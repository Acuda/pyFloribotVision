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
from .. BasePlugin import BasePlugin
import cv2
import logging
import numpy as np


class HStack(BasePlugin):

    configParameter = [
        ImageType('inputImageL', input=True),
        ImageType('inputImageR', input=True),
        ImageType('outputImage', output=True),
    ]

    def __init__(self, **kwargs):
        super(HStack, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        self.outputImage.data = np.hstack((self.inputImageL.data, self.inputImageR.data))

