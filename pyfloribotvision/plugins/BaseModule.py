#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

import logging
import copy
#from pyfloribotvision.manager.DependencyManager import DependencyManager


#class BaseModule(DependencyManager):
class BaseModule(object):

    # must have options in the config file
    # provided as dict(), keys are the option names
    # values are a list() of allowed values if they are constricted
    # if set in subclass, these options will be loaded automatically from baseclass
    obligatoryConfigOptions = dict()

    def __init__(self, **kwargs):
        self.activeModule = True  # needs to be before the DependencyManager
        #super(BaseModule, self).__init__(**kwargs)

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.sectionConfig = kwargs['sectionConfig']
        self.ioContainer = kwargs['ioContainer']
        self.logicSectionName = kwargs['logicSectionName']

        self.log.debug('invoked by subclass <%s> for logicSectionName <%s> ',
                       type(self).__name__, self.logicSectionName)

        self.loadOptions()


        if self.activeModule:
            self.postOptActions()
        else:
            self.log.warning('plugin <%s> for section <%s> NOT active! skipping postOptActions',
                             self.logicSectionName, type(self).__module__)



    def loadOptions(self):
        self.configParameter = copy.deepcopy(self.configParameter)
        for parameter in self.configParameter:
            parameter._logicSectionName = self.logicSectionName
            parameter.initLog()
            if parameter.name not in self.sectionConfig:
                self.log.error('option <%s> for section <%s> missing, requested for plugin <%s>, '
                               'setting plugin for section as inactive', parameter.name, self.logicSectionName,
                               type(self).__module__)
                self.activeModule = False
                continue

            parameter.value = self.sectionConfig[parameter.name]
            self.sectionConfig[parameter.name] = parameter

            #if value is not None and confValue not in value:
            #    self.log.error('constrained option <%s> with invalid value <%s> found! valid '
            #                   'values are <%s>', key, confValue, value)

            self.__dict__[parameter.name] = parameter
            self.log.debug('dynamic attribute <%s> with value <%s> created',
                           parameter.name, self.__dict__[parameter.name])

    def timeBypassActions(self):
        self.log.debug('function timeBypassActions() is not overloaded in subclass <%s>',
                       type(self).__name__)

    def postOptActions(self):
        self.log.debug('function externalCall() is not overloaded in subclass <%s>',
                       type(self).__name__)

    def externalCall(self):
        #self.updateDependency()
        self.log.debug('function externalCall() is not overloaded in subclass <%s>!',
                         type(self).__name__)

    def preOptActions(self):
        self.log.debug('function preOptActions() is not overloaded in subclass <%s>',
                       type(self).__name__)
