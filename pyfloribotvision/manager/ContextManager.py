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
from pyfloribotvision.controller.PluginController import PluginController
from pyfloribotvision.controller.ConfigController import ConfigController
from pyfloribotvision.controller.DataLinkController import DataLinkController
from pyfloribotvision.manager.ProcessManager import ProcessManager


class ContextManager(object):
    """Prepare Application-Context and give the ability to access the Context trough normal
    initialisation for a given Pseudo-Namespace. The ContextManager provides the Plugins-,
    Configuration- and DataLink-Controller as well as the ProcessManager. """

    _instance = dict()

    def __new__(cls, *args, **kwargs):
        """
        Act as singleton for simpler data sharing. Internal use only!

        :param args:
        :param kwargs:
        """
        ctxName = args[0] if args else None

        if ctxName not in cls._instance.keys():
            cls._instance[ctxName] = super(ContextManager, cls).__new__(cls, *args, **kwargs)

        return cls._instance[ctxName]

    def __init__(self, contextName=None):
        """Initialize a new instance per given contextName. Every new init for a known contextName
        returns previously initialized instance for corresponding context.

        :param contextName: specifies the context (default ``None``)
        """
        self.pluginController = None
        self.configController = None
        self.dataLinkController = None
        self.processManager = None

    def initContext(self, configFileName, loggingConfigFileName, pluginprefix):
        """Initializes the Controller, Manager and Logger for given configuration data.

        :param configFileName: Configuration-File for the ConfigController
        :param loggingConfigFileName: Configuration-File for the Logger
        :param pluginprefix: Prefix where the Plugin-Package can be found
        """
        logging.config.fileConfig(loggingConfigFileName)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        if self.pluginController is None:
            self.pluginController = PluginController(pluginprefix)

        if self.configController is None:
            self.configController = ConfigController(configFileName)

        if self.dataLinkController is None:
            self.dataLinkController = DataLinkController()

        if self.processManager is None:
            self.processManager = ProcessManager(self.pluginController, self.configController,
                                                 self.dataLinkController)

    def executeContext(self):
        """Triggers the executePlugins Method from the ProcessManager"""
        self.processManager.executePlugins()