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
from pyfloribotvision.types.IntListType import IntListType
from .. BaseModule import BaseModule
import cv2
import logging


class CVStructuringElement(BaseModule):

    configParameter = [
        StringType('cvShape'),
        NameType('outputElementName', output=True),
        IntListType('cvKSize'),
    ]

    obligatoryConfigOptions = {'outputElementName': None, 'cvShape': None, 'cvKSize': None}

    def __init__(self, **kwargs):
        super(CVStructuringElement, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        if not hasattr(cv2, self.cvShape.value):
            self.log.error('unknown cvShape <%s>, deactivating module <%s>', self.cvShape.value, self.logicSectionName)
            self.activeModule = False
        else:
            self.cvShape.data = getattr(cv2, self.cvShape.value)

    def externalCall(self):
        element = cv2.getStructuringElement(self.cvShape.data, self.cvKSize.getConvertedValue(tuple))
        self.outputElementName.data = element
