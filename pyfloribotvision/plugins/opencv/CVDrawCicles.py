#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.IntListType import IntListType
from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.IntType import IntType
from pyfloribotvision.types.BoolType import BoolType
from .. BasePlugin import BasePlugin
import cv2
import logging
import numpy as np


class CVDrawCicles(BasePlugin):
    """
    if inputContourIndexListName is empty, then draw all contours
    """

    configParameter = [
        ImageType('inputImageName', input=True),
        StringType('circleData', input=True),
        ImageType('outputImageName', output=True),
        BoolType('binarizedOutput'),
        IntListType('color'),
        IntType('thickness'),
    ]

    def __init__(self, **kwargs):
        super(CVDrawCicles, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):

        if self.binarizedOutput.value:
            if len(self.inputImageName.data.shape) > 1:
                image = np.zeros(tuple(self.inputImageName.data.shape[:2]), np.uint8)
            else:
                image = np.zeros_like(self.inputImageName.data)
        else:
            image = self.inputImageName.data.copy()

        if self.circleData.data is not None:
            for circ in self.circleData.data[0]:
                cv2.circle(image, (circ[0], circ[1]), circ[2], self.color.value, self.thickness.value)

        self.outputImageName.data = image


