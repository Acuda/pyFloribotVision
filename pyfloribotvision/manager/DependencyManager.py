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
#from .. plugins.BaseModule import BaseModule

class DependencyManager(object):

    def __init__(self, **kwargs):
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.sectionConfig = kwargs['sectionConfig']
        self.ioContainer = kwargs['ioContainer']
        self.logicSectionName = kwargs['logicSectionName']



        self.loadOptions()


    def loadOptions(self):
        self.log.debug('loadOptions invoked')
        for key, value in self.obligatoryConfigOptions.items():

            if key not in self.sectionConfig:
                self.log.error('option <%s> for section <%s> missing, requested for plugin <%s>, '
                               'setting plugin for section as inactive', key, self.logicSectionName,
                               type(self).__module__)
                self.activeModule = False
                continue

            confValue = self.sectionConfig[key]

            if value is not None and confValue not in value:
                self.log.error('constrained option <%s> with invalid value <%s> found! valid '
                               'values are <%s>', key, confValue, value)

            self.__dict__[key] = self.sectionConfig[key]
            self.log.debug('dynamic attribute <%s> with value <%s> created',
                           key, self.__dict__[key])

