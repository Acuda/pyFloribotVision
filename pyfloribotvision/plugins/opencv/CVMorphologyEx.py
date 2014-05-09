#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import logging


class CVMorphologyEx(BasePlugin):

    configParameter = [
        StringType('cvOperation'),
        NameType('inputImageName', input=True),
        NameType('inputElementName', input=True),
        NameType('outputImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(CVMorphologyEx, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        if not hasattr(cv2, self.cvOperation.value):
            self.log.error('unknown cvOperation <%s>, deactivating module <%s>', self.cvOperation,
                           self.logicSectionName)
            self.activeModule = False
        else:
            self.cvOperation.data = getattr(cv2, self.cvOperation.value)


    def externalCall(self):
        image = cv2.morphologyEx(self.inputImageName.data, self.cvOperation.data,
                                 self.inputElementName.data)
        self.outputImageName.data = image


