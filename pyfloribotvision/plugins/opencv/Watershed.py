#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging


class Watershed(BasePlugin):

    configParameter = [
        NameType('inputImage', input=True),
        NameType('inputImageBackground', input=True),
        NameType('inputImageForeground', input=True),
        NameType('outputImage', output=True),
    ]

    def __init__(self, **kwargs):
        super(Watershed, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def externalCall(self):
        image = self.inputImage.data
        foreground = self.inputImageForeground.data
        background = self.inputImageBackground.data

        foreground = foreground.copy()


        ret, bg = cv2.threshold(background, 1, 128, 1)


        marker = cv2.add(foreground, bg)

        cv2.imshow('marker ', marker )

        marker32 = np.int32(marker)

        cv2.watershed(image, marker32)
        m = cv2.convertScaleAbs(marker32)

        cv2.imshow('m', m)
        self.outputImage.data = m