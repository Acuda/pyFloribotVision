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
from pyfloribotvision.types.IntListType import IntListType
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import logging
import numpy as np

class CVDrawContours(BasePlugin):
    """
    if inputContourIndexListName is empty, then draw all contours
    """

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        NameType('inputContourName', input=True),
        IntType('thickness'),
        NameType('inputContourIndexListName', input=True),
        IntListType('contourColor'),
    ]

    def __init__(self, **kwargs):
        super(CVDrawContours, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        if self.inputContourIndexListName.data:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(self.inputContourName.data))

        imagecpy = self.inputImageName.data.copy()
        for cidx in contidx:
            cv2.drawContours(imagecpy, self.inputContourName.data, cidx, color=self.contourColor, thickness=self.thickness.value)
        self.outputImageName.data = imagecpy


