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
import numpy as np
import logging


class CVInRange(BaseModule):

    obligatoryConfigOptions = {'inputImageName': None, 'outputMaskListNames': None, 'cvValueListNames': None}

    def __init__(self, **kwargs):
        super(CVInRange, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        self.cvValueListNames = self.cvValueListNames.replace(' ', '').split(',')
        self.outputMaskListNames = self.outputMaskListNames.replace(' ', '').split(',')

    def externalCall(self):
        for k, v in enumerate(self.cvValueListNames[::2]):
            self.log.debug('inRange action Nr. <%s> for inputImageName <%s> creating image <%s>', k, self.inputImageName, self.outputMaskListNames[k])
            self.log.debug('checking lower border <%s> up to upper border <%s>', self.ioContainer[v], self.ioContainer[self.cvValueListNames[k*2+1]])
            imagebin = cv2.inRange(self.ioContainer[self.inputImageName],
                                   self.ioContainer[v],
                                   self.ioContainer[self.cvValueListNames[k*2+1]])
            self.ioContainer[str(self.outputMaskListNames[k])] = imagebin
