#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import logging


class CVFindContours(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputContourName', output=True),
        NameType('outputHierarchyName', output=True),
        StringType('cvMode'),
        StringType('cvMethod'),
    ]


    def __init__(self, **kwargs):
        super(CVFindContours, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        self.cvMode.value = self.cvMode.value.upper()
        self.cvMethod.value = self.cvMethod.value.upper()

        if not hasattr(cv2, self.cvMode.value):
            self.log.error('unknown cvMode <%s>, detaching module <%s>', self.cvMode,
                           self.logicSectionName)
            self.activeModule = False
        else:
            self.cvMode.data = getattr(cv2, self.cvMode.value)

        if not hasattr(cv2, self.cvMethod.value):
            self.log.error('unknown cvMethod <%s>, detaching module <%s>', self.cvMode,
                           self.logicSectionName)
            self.activeModule = False
        else:
            self.cvMethod.data = getattr(cv2, self.cvMethod.value)

    def externalCall(self):
        cont, h = cv2.findContours(self.inputImageName.data, mode=self.cvMode.data,
                                   method=self.cvMethod.data)
        self.outputContourName.data = cont
        self.outputHierarchyName.data = h