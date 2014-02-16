#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import cv2
import logging


class CVFindContours(BaseModule):
    obligatoryConfigOptions = {'inputImageName': None, 'outputContourName': None, 'outputHierarchyName': None,
                               'cvMode': None, 'cvMethod': None}



    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        self.cvMode = self.cvMode.upper()
        self.cvMethod = self.cvMethod.upper()

        if not hasattr(cv2, self.cvMode):
            self.log.error('unknown cvMode <%s>, detaching module <%s>', self.cvMode, self.logicSectionName)
            self.activeModule = False
        else:
            self.cvMode = getattr(cv2, self.cvMode)

        if not hasattr(cv2, self.cvMethod):
            self.log.error('unknown cvMethod <%s>, detaching module <%s>', self.cvMode, self.logicSectionName)
            self.activeModule = False
        else:
            self.cvMethod = getattr(cv2, self.cvMethod)

    def externalCall(self):
        cont, h = cv2.findContours(self.ioContainer[self.inputImageName], mode=self.cvMode, method=self.cvMethod)
        self.ioContainer[self.outputContourName] = cont
        self.ioContainer[self.outputHierarchyName] = h