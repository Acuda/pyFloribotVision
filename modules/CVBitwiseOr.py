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
import numpy as np
import logging


class CVBitwiseOr(BaseModule):

    obligatoryConfigOptions = {'inputImageName1': None, 'inputImageName2': None, 'outputImageName': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        image1 = self.ioContainer[self.inputImageName1]
        image2 = self.ioContainer[self.inputImageName2]
        image = np.zeros(image1.shape, np.uint8)
        cv2.bitwise_or(image1, image2, image)
        self.ioContainer[self.outputImageName] = image