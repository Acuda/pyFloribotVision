#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import cv2
import logging


class ApplyColorMap(BaseModule):
    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None,
                               'colorMapCode': None}


    def __init__(self, **kwargs):
        super(ApplyColorMap, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def postOptActions(self):
        self.colorMapCode = self.colorMapCode.upper()

        if not hasattr(cv2, self.colorMapCode):
            self.log.error('unknown colorMapCode <%s>, detaching module <%s>', self.colorMapCode,
                           self.logicSectionName)
            self.activeModule = False



    def externalCall(self):
        image = self.ioContainer[self.inputImageName]
        image = cv2.applyColorMap(image, getattr(cv2, self.colorMapCode))
        self.ioContainer[self.outputImageName] = image
