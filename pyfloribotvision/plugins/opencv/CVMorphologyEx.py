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


class CVMorphologyEx(BaseModule):
    obligatoryConfigOptions = {'cvOperation': None, 'inputImageName': None, 'inputElementName': None,
                               'outputImageName': None}

    def __init__(self, **kwargs):
        super(CVMorphologyEx, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        if not hasattr(cv2, self.cvOperation):
            self.log.error('unknown cvOperation <%s>, deactivating module <%s>', self.cvOperation, self.logicSectionName)
            self.activeModule = False
        else:
            self.cvOperation = getattr(cv2, self.cvOperation)


    def externalCall(self):

        image = cv2.morphologyEx(self.ioContainer[self.inputImageName], self.cvOperation,
                                 self.ioContainer[self.inputElementName])
        self.ioContainer[self.outputImageName] = image


