#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.StringType import StringType
from .. BaseModule import BaseModule
import cv2
import logging


class ApplyColorMap(BaseModule):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        StringType('colorMapCode'),
    ]

    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None,
                               'colorMapCode': None}


    def __init__(self, **kwargs):
        super(ApplyColorMap, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def postOptActions(self):
        self.colorMapCode.value = self.colorMapCode.value.upper()

        if not hasattr(cv2, self.colorMapCode.value):
            self.log.error('unknown colorMapCode <%s>, detaching module <%s>',
                           self.colorMapCode.value, self.logicSectionName)
            self.activeModule = False



    def externalCall(self):
        self.outputImageName.data = cv2.applyColorMap(self.inputImageName.data,
                                                     getattr(cv2, self.colorMapCode.value))

