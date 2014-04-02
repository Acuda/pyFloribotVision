#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import numpy as np
import logging

class CVValueList(BaseModule):

    obligatoryConfigOptions = {'inputValues': None, 'inputType': None, 'outputNames': None,
                               'runCycle': ['oneShoot', 'loop']}

    def __init__(self, **kwargs):
        super(CVValueList, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):

        self.inputValues = [np.array(item.split(','), np.uint8)
                            for item in self.inputValues.replace(' ', '').split(';')]
        self.outputNames = self.outputNames.replace(' ', '').split(',')


    def externalCall(self):

        for k, v in enumerate(self.outputNames):
            self.ioContainer[v] = self.inputValues[k]

        self.activeModule = False

        #self.moduleControllerInstance.detachModule(self)

