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
from controller.PluginController import PluginController
from controller.ConfigController import ConfigController
from controller.DataLinkController import DataLinkController



class ProcessManager(object):

    _SECTIONNAME = 'GENERAL'

    def __init__(self, pluginController, configController, dataLinkController):

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        assert isinstance(pluginController, PluginController)
        self.pluginController = pluginController

        assert isinstance(configController, ConfigController)
        self.configController = configController

        assert isinstance(dataLinkController, DataLinkController)
        self.dataLinkController = dataLinkController

        self.ownConfig = self.configController.getSection(self._SECTIONNAME)

        self.pluginSequence = self.acquireLogicSections()
        self.pluginPath = self.acquirePluginPath()

        # ToDo: Instantiate Plugins, Run-Stuff, etc.

    def acquireLogicSections(self):
        return [x for x in utils.configStrToList(self.ownConfig['pluginSequence']) if
                not x.startswith('!')]

    def acquirePluginPath(self, pluginSequence=None):
        if not pluginSequence:
            pluginSequence = self.pluginSequence

        pluginPathList = list()
        for section in pluginSequence:
            pluginPathList.append(self.configController.getOption(section, 'pluginPath'))

        return pluginPathList


