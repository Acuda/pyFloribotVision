#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


import logging
import copy


class BasePlugin(object):

    # provided as list(), items must be a subclass of types.BaseType
    # the name of the parameter in the config-file is needet for the constructor
    # of the used type. if needed, the parameter can be set as in- or output by a
    #  optional second parameter (input=True / output=True)
    #  e.g.: configParameter = [SomeType('inputParameter', input=True)]

    configParameter = list()  # overwritten by subclasses (obligatory!)

    def __init__(self, **kwargs):
        self.activeModule = True  # needs to be before the DependencyManager
        #super(BasePlugin, self).__init__(**kwargs)

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.sectionConfig = kwargs['sectionConfig']
        #self.ioContainer = kwargs['ioContainer']
        self.logicSectionName = kwargs['logicSectionName']

        self.log.debug('invoked by subclass <%s> for logicSectionName <%s> ',
                       type(self).__name__, self.logicSectionName)

        self.loadOptions()

        if self.activeModule:
            pass  # self.preCyclicCall()
        else:
            self.log.warning('plugin <%s> for section <%s> NOT active! '
                             'skipping preCyclicCall',
                             self.logicSectionName, type(self).__module__)


    def loadOptions(self, obj=None):
        # keep at the following line in mind, that self.configParameter is static
        # and refers to the same memory on all instances of the same plugin class.
        # therefore we have to duplicate the static-data to a new _un_static memory

        if obj is None:
            obj = self

        self.log.debug('try to load and inject configuration')

        obj.configParameter = copy.deepcopy(obj.configParameter)
        for parameter in obj.configParameter:
            parameter._logicSectionName = obj.logicSectionName
            parameter.initLog()
            if parameter.name not in obj.sectionConfig:
                obj.log.error('option <%s> for section <%s> missing, '
                               'requested for plugin <%s>, '
                               'setting plugin for section as inactive',
                               parameter.name, obj.logicSectionName,
                               type(obj).__module__)
                obj.activeModule = False
                continue

            parameter.value = obj.sectionConfig[parameter.name]
            obj.sectionConfig[parameter.name] = parameter

            obj.__dict__[parameter.name] = parameter
            obj.log.debug('dynamic attribute <%s> with value <%s> created',
                           parameter.name, parameter.value)

    def preCyclicCall(self):
        self.log.debug('function preCyclicCall is not overloaded in subclass <%s>',
                       type(self).__name__)

    def externalCall(self):
        #self.updateDependency()
        self.log.debug('function externalCall is not overloaded in subclass <%s>!',
                         type(self).__name__)

    def timeBypassActions(self):
        self.log.debug('function timeBypassActions is not overloaded in subclass '
                       '<%s>', type(self).__name__)

    def postCyclicCall(self):
        self.log.debug('function postCyclicCall is not overloaded in subclass <%s>',
                       type(self).__name__)
