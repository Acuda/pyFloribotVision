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
from pyfloribotvision.dto.PluginDTO import PluginDTO
import time
import cv2


class ProcessManager(object):

    _SECTIONNAME = 'GENERAL'

    def __init__(self, pluginController, configController, dataLinkController):

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

        self.pluginDtoList = self.aquirePlugins()
        self.instantiatePlugins()

        # Cycle-Specific (execute Plugins / handle runtime characteristics)
        ####################################################################

        self.cycleTimeLast = 0

        # ToDo: Instantiate Plugins, Run-Stuff, etc.

    def aquirePlugins(self, generalConfigSection=None):
        self.log.debug('enter aquirePlugins')
        if generalConfigSection is None:
            generalConfigSection = self.ownConfig['pluginSequence']
        if generalConfigSection is None:
            return None

        pluginDtoList = list()
        for section in utils.configStrToList(generalConfigSection):
            if not section.startswith('!'):
                pdto = PluginDTO()
                pdto.sectionName = section
                pdto.modulePath = self.configController.getOption(section, 'pluginPath')
                pdto.classObject = self.pluginController.findPlugin(pdto.modulePath)
                if pdto.classObject is None:
                    continue
                pluginDtoList.append(pdto)
        return pluginDtoList

    def instantiatePlugins(self, pluginDtoList=None):
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

        grabFrameTime = int(self.ownConfig['grabFrameTime']) / 1000.0
        runCycle = self.ownConfig['runCycle']
        exitKey = self.ownConfig['exitKey']

        self.log.debug('=' * 30 + ' RUN ACTIVE MODULES ' + '=' * 30)

        while True:
            if (time.time() - self.cycleTimeLast) > grabFrameTime:
                self.triggerPluginMethods('externalCall')
                self.cycleTimeLast = time.time()
            else:
                self.triggerPluginMethods('timeBypassActions')

            if runCycle == 'oneShoot':
                break

            if (cv2.waitKey(1) & 255) == ord(exitKey):
                break

        self.triggerPluginMethods('preOptActions')

    def triggerPluginMethods(self, functionName, pluginDtoList=None):
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

            moduleFunction = getattr(pdtoObj, functionName)
            moduleFunction()
