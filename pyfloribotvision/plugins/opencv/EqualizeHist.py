#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.StringType import StringType
from .. BasePlugin import BasePlugin
import logging
import cv2
from cv2 import cv
import numpy as np

class EqualizeHist(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
        ImageType('outputImage', output=True),
    ]

    def __init__(self, **kwargs):
        super(EqualizeHist, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        ch = 2
        image = self.inputImage.data
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[...,ch] = cv2.equalizeHist(hsv[...,ch])



        image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        #size = image.shape[0]
        #cv2.circle(image, (image.shape[1]//2,image.shape[0]+size//2), size, (0,0,0), -1)

        self.outputImage.data = image




