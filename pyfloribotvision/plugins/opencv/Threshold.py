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
from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging


class Threshold(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
        ImageType('outputImage', output=True),
        IntType('threshold'),
        IntType('max'),
        IntType('type'),
    ]

    def __init__(self, **kwargs):
        super(Threshold, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        image = self.inputImage.data
        ret, image = cv2.threshold(image, self.threshold.value, self.max.value, self.type.value)
        self.outputImage.data = image

