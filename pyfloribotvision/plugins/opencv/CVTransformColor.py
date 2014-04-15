#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.StringType import StringType
from .. BaseModule import BaseModule
import cv2
import logging

class CVTransformColor(BaseModule):

    configParameter = [
        NameType('inputImageName', input=True), NameType('outputImageName', output=True),
        StringType('colorCode'),
    ]

    def __init__(self, **kwargs):
        super(CVTransformColor, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        self.colorCode.value = self.colorCode.value.upper()

        if not hasattr(cv2, self.colorCode.value):
            self.log.error('unknown colorCode <%s>, detaching module <%s>', self.colorCode.value,
                           self.logicSectionName)
            self.activeModule = False

    def externalCall(self):
        #image = self.ioContainer[self.inputImageName]
        image = self.inputImageName.data
        image = cv2.cvtColor(image, getattr(cv2, self.colorCode.value))
        self.outputImageName.data = image
        #self.ioContainer[self.outputImageName] = image