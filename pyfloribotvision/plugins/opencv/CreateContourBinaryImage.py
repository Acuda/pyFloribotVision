#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from ..BasePlugin import BasePlugin
import cv2
import logging
import numpy as np


class CreateContourBinaryImage(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('inputContourName', input=True),
        NameType('inputContourIndexListName', input=True),
        NameType('outputImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(CreateContourBinaryImage, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        shape = tuple(self.inputImageName.data.shape[0:2])
        image = np.zeros(shape, np.uint8)

        if self.inputContourIndexListName.data:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(self.inputContourName.data))

        shape = list(image.shape[0:2])
        shape.insert(0, len(contidx))
        shape = tuple(shape)

        ccimage = np.zeros(shape, np.uint8)

        for k, v in enumerate(contidx):
            cv2.drawContours(ccimage[k], self.inputContourName.data, v, (255, 255, 255), -1)

        self.outputImageName.data = ccimage[0] if len(contidx) > 0 else image