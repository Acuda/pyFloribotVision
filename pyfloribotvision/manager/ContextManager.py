#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.

from __future__ import print_function
import logging
import logging.config
from controller.PluginControlller import PluginController
from controller.ConfigController import ConfigController
from controller.DataLinkController import DataLinkController


class ContextManager(object):

    _instance = dict()

    def __new__(cls, *args, **kwargs):
        """
        Act as singleton for simpler data sharing. Internal use only!
        """
        ctxName = args[0] if args else None

        if ctxName not in cls._instance.keys():
            cls._instance[ctxName] = super(ContextManager, cls).__new__(cls, *args, **kwargs)

        return cls._instance[ctxName]

    def __init__(self, contextName=None):
        self.pluginController = None
        self.configController = None
        self.dataLinkController = None
        self.processManager = None

    def initContext(self, configFileName, loggingConfigFileName):
        logging.config.fileConfig(loggingConfigFileName)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        if not self.pluginController:
            self.pluginController = PluginController()

        if not self.configController:
            self.configController = ConfigController(configFileName)

        if not self.dataLinkController:
            self.dataLinkController = DataLinkController()
