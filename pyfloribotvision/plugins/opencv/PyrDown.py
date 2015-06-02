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
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import logging


class PyrDown(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
        ImageType('outputImage', output=True),
        IntType('times'),
    ]

    def __init__(self, **kwargs):
        super(PyrDown, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        image = self.inputImage.data
        for i in range(self.times.value):
            image = cv2.pyrDown(image)
        self.outputImage.data = image

