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
from pyfloribotvision.types.BoolType import BoolType
from .. BasePlugin import BasePlugin
import logging
import cv2
import numpy as np


class NewImage(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        ImageType('outputImageName', output=True),
        BoolType('likeImage'),
        IntType('width'),
        IntType('height'),
        IntType('depth'),

    ]

    def __init__(self, **kwargs):
        super(NewImage, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):

        if self.likeImage.value:
            image = np.zeros_like(self.inputImageName.data)
        else:
            shape = list()
            if self.height.value > 0:
                shape.append(self.height.value)
            if self.width.value > 0:
                shape.append(self.width.value)
            if self.depth.value > 0:
                shape.append(self.depth.value)
            shape = tuple(shape)

            image = np.zeros(shape)
        self.outputImageName.data = image