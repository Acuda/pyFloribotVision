#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from BaseModule import BaseModule
import cv2
import logging


class CVStructuringElement(BaseModule):
    obligatoryConfigOptions = {'outputElementName': None, 'cvShape': None, 'cvKSize': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        if not hasattr(cv2, self.cvShape):
            self.log.error('unknown cvShape <%s>, deactivating module <%s>', self.cvShape, self.logicSectionName)
            self.activeModule = False
        else:
            self.cvShape = getattr(cv2, self.cvShape)

        self.cvKSize = tuple([int(x) for x in self.cvKSize.replace(' ', '').split(',')])

    def externalCall(self):
        element = cv2.getStructuringElement(self.cvShape, self.cvKSize)
        self.ioContainer[self.outputElementName] = element
