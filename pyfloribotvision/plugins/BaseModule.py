#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

import logging


class BaseModule(object):

    # must have options in the config file
    # provided as dict(), keys are the option names
    # values are a list() of allowed values if they are constricted
    # if set in subclass, these options will be loaded automatically from baseclass
    obligatoryConfigOptions = dict()

    def __init__(self, **kwargs):
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.sectionConfig = kwargs['sectionConfig']
        self.ioContainer = kwargs['ioContainer']
        self.logicSectionName = kwargs['logicSectionName']

        self.activeModule = True

        self.log.debug('invoked by subclass <%s> for logicSectionName <%s> ',
                       type(self).__name__, self.logicSectionName)

        self.loadOptions()
        self.postOptActions()

    def loadOptions(self):

        # ToDo:
        # real autoload of values to real objects
        # eg. inputImageName = asd should result in self.inputImageName = real image from ioContainer so that
        # the step to get the image myself via self.ioContaint[self.inputImageName] is needless
        # note: check if name is in ioContainer, if not plain values are applied
        # eg. value = 1,2,3 -> 1,2,3 is not a key so 1,2,3 must be values (hard map to int possible?)
        # furthermore a list should handled the same
        #
        # note: loadOptions is triggered only once... so there shoud be a nice way do bypass this...
        # decorators? if source is ioContainer -> decorator for reallogation at access once per cycle
        #
        # TestFile is ConfInputParseSample

        self.log.debug('loadOptions invoked')
        for key, value in self.obligatoryConfigOptions.items():
            confValue = self.sectionConfig[key]

            if value is not None and confValue not in value:
                self.log.error('constrained option <%s> with invalid value <%s> found! valid values are <%s>',
                               key, confValue, value)

            self.__dict__[key] = self.sectionConfig[key]
            self.log.debug('dynamic attribute <%s> with value <%s> created', key, self.__dict__[key])

    def timeBypassActions(self):
        self.log.debug('function timeBypassActions() is not overloaded in subclass <%s>', type(self).__name__)

    def postOptActions(self):
        self.log.debug('function externalCall() is not overloaded in subclass <%s>', type(self).__name__)

    def externalCall(self):
        self.log.warning('function externalCall() is not overloaded in subclass <%s>!', type(self).__name__)

    def preOptActions(self):
        self.log.debug('function preOptActions() is not overloaded in subclass <%s>', type(self).__name__)
