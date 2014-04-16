#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.

import logging
import utils
from pyfloribotvision.controller.PluginController import PluginController
from pyfloribotvision.controller.ConfigController import ConfigController
from pyfloribotvision.controller.DataLinkController import DataLinkController
from pyfloribotvision.types.BaseType import BaseType
from pyfloribotvision.dto.PluginDTO import PluginDTO
import time
import cv2


class ProcessManager(object):
    """Manages the Process and is responsibly for the runtime behavior"""

    _SECTIONNAME = 'GENERAL'

    def __init__(self, pluginController, configController, dataLinkController):
        """Gets the 'GENERAL' section from the ConfigController and acquires and instantiate the
        Plugins specified by the 'pluginSequence' Option in the Configuration

        :param pluginController: Instance of the ``PluginController``
        :param configController: Instance of the ``ConfigController``
        :param dataLinkController: Instance of the ``DataLinkController``
        """

        # Logging
        ##########

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        # ProcessStuff
        ###############

        assert isinstance(pluginController, PluginController)
        self.pluginController = pluginController

        assert isinstance(configController, ConfigController)
        self.configController = configController

        assert isinstance(dataLinkController, DataLinkController)
        self.dataLinkController = dataLinkController

        # Init-Specific (Config / Plugins)
        ###################################

        self.ownConfig = self.configController.getSection(self._SECTIONNAME)

        self.pluginDtoList = self.acquirePlugins()
        self.instantiatePlugins()

        # Cycle-Specific (execute Plugins / handle runtime characteristics)
        ####################################################################

        #self.cycleTimeLast = 0
        curTime = time.time()
        self.lastExecTime = curTime
        self.lastBypassTime = curTime
        self.lastCycleTime = curTime

        self.deltaExecTime = 0
        self.deltaBypassTime = 0

    def acquirePlugins(self, generalConfigSection=None):
        """Acquire the Plugins specified by the 'pluginSequence' Option in the Configuration given
        by the dict generalConfigSection or internal config if generalConfigSection is None.
        Furthermore returns a list of PluginDto for each loaded Plugin whose Name in the
        pluginSequence Option don't start with an exclamation mark

        :param generalConfigSection: Config for 'GENERAL' section (default ``None``)
        """

        self.log.debug('enter acquirePlugins')
        if generalConfigSection is None:
            generalConfigSection = self.ownConfig['pluginSequence']
        if generalConfigSection is None:
            return None

        pluginDtoList = list()
        for section in utils.configStrToList(generalConfigSection):
            if not section.startswith('!'):
                pdto = PluginDTO()
                pdto.sectionName = section
                try:
                    pdto.modulePath = self.configController.getOption(section, 'pluginPath')
                except AssertionError as e:
                    self.log.critical('asd %s', e.message)

                pdto.classObject = self.pluginController.loadPluginClass(pdto.modulePath)
                if pdto.classObject is None:
                    continue
                pluginDtoList.append(pdto)
        return pluginDtoList

    def instantiatePlugins(self, pluginDtoList=None):
        """Instantiate the Plugins in the list of PluginDto's and return the List

        :param pluginDtoList: List of PluginDto's (default None)
        """

        self.log.debug('enter instantiatePlugins')
        self.log.debug('check pluginDtoList')
        if pluginDtoList is None:
            self.log.debug('load private data')
            pluginDtoList = self.pluginDtoList
        if pluginDtoList is None:
            return None

        self.log.debug('instantiate Plugins')
        for pdto in pluginDtoList:
            assert isinstance(pdto, PluginDTO)
            self.log.debug('instantiate Plugin <%s> for Section <%s>', pdto.modulePath, pdto.sectionName)
            sectionConfig = self.configController.getSection(pdto.sectionName)
            pdto.instanceObject = pdto.classObject(sectionConfig=sectionConfig,
                                                   logicSectionName=pdto.sectionName,
                                                   ioContainer=self.dataLinkController)


    def executePlugins(self, pluginDtoList=None):
        if pluginDtoList is None:
            pluginDtoList = self.pluginDtoList
        assert isinstance(pluginDtoList, list)

        leadTime = int(self.ownConfig['leadTime']) / 1000.0
        waitLeadTime = self.ownConfig['waitLeadTime'] == str(True)
        runOnce = self.ownConfig['runOnce'] == str(True)
        exitKey = self.ownConfig['exitKey']

        self.log.debug('')
        self.log.debug('=' * 30 + ' REGISTER DEPENDENCY ' + '=' * 30)
        self.registerDependency()

        self.log.debug('')
        self.log.debug('=' * 30 + ' RUN ACTIVE MODULES ' + '=' * 30)


        isFirstRun = True
        while True:
            curTime = time.time()
            deltaExec = curTime - self.lastExecTime

            if isFirstRun or (deltaExec + self.deltaBypassTime) > leadTime:
                waitTime = leadTime - deltaExec

                if waitLeadTime and not isFirstRun and waitTime > 0:
                    time.sleep(waitTime)
                if leadTime != 0 and waitTime < 0:
                    self.log.warn('LeadTime <%d> unreachable!')

                self.lastExecTime = time.time()
                self.triggerPluginMethods('externalCall')
                self.deltaExecTime = time.time() - self.lastExecTime
            else:
                self.lastBypassTime = time.time()
                self.triggerPluginMethods('timeBypassActions')
                self.deltaBypassTime = time.time() - self.lastBypassTime

            isFirstRun = False

            if runOnce:
                break

            if (cv2.waitKey(1) & 255) == ord(exitKey):
                break


        self.triggerPluginMethods('preOptActions')

    def triggerPluginMethods(self, methodName, pluginDtoList=None):
        """Triggers the corresponding methods of the active Plugins in the pluginDtoList

        :param methodName: Name of the Plugin-Method to trigger
        :param pluginDtoList: List of PluginDto's (default None)
        """

        if pluginDtoList is None:
            pluginDtoList = self.pluginDtoList
        assert isinstance(pluginDtoList, list)

        for pdto in pluginDtoList:
            assert isinstance(pdto, PluginDTO)
            pdtoObj = pdto.instanceObject
            if not pdtoObj.activeModule:
                self.log.debug('Skipping inactive Module <%s> for logical Section <%s>',
                               pdtoObj.__class__.__name__, pdtoObj.logicSectionName)
                continue

            self.log.debug('Calling Module <%s> for logical Section <%s>',
                           pdtoObj.__class__.__name__, pdtoObj.logicSectionName)

            moduleFunction = getattr(pdtoObj, methodName)
            moduleFunction()

    def registerDependency(self, pluginDtoList=None):

        if pluginDtoList is None:
            pluginDtoList = self.pluginDtoList
        assert isinstance(pluginDtoList, list)

        inputParameter = dict()
        outputParameter = dict()


        self.log.debug('')
        self.log.debug('-' * 30 + ' PreLoad I/O-Parameter ' + '-' * 30)
        for pdto in pluginDtoList:
            self.log.debug('.' * 20 + ' <%s> ' + '.' * 20, pdto.instanceObject.logicSectionName)
            assert isinstance(pdto, PluginDTO)
            baseTypeParameter = [x for x in pdto.instanceObject.sectionConfig.values()
                                 if issubclass(type(x), BaseType) and (x.output or x.input)]

            for x in baseTypeParameter:
                if x.input:
                    self.log.debug('input found:')
                    self.attachToDependencyIOList(x, inputParameter)

                if x.output:
                    self.log.debug('output found:')
                    self.attachToDependencyIOList(x, outputParameter)

        self.log.debug('')
        self.log.debug('-' * 30 + ' Wire I/O-Callbacks for Parameter-Types ' + '-' * 30)

        for oname, opara in outputParameter.items():
            if oname in inputParameter:
                for output in opara:
                    for ipara in inputParameter[oname]:
                        self.log.debug('parameter <%s> for value <%s> to <%s> on value <%s> ',
                                       output.name, output.value, ipara.value, ipara.name)
                        output.registerDataUpdate(ipara.dataUpdateCallback)


    def attachToDependencyIOList(self, para, dstList):


        valueList = para.value
        if not isinstance(valueList, list):
            valueList = [valueList]

        for value in valueList:
            if value not in dstList:
                dstList[value] = list()

            self.log.debug('parameter <%s> for value <%s>', para.name, value)
            dstList[value].append(para)


