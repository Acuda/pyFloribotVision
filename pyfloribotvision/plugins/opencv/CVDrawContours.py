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
from pyfloribotvision.types.IntListType import IntListType
from .. BaseModule import BaseModule
import cv2
import logging


class CVDrawContours(BaseModule):
    """
    if inputContourIndexListName is empty, then draw all contours
    """

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        NameType('inputContourName', input=True),
        NameType('inputContourIndexListName', input=True),
        IntListType('contourColor'),
    ]

    def __init__(self, **kwargs):
        super(CVDrawContours, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        if self.inputContourIndexListName in self.ioContainer:
            contidx = self.ioContainer[self.inputContourIndexListName]
        else:
            contidx = range(len(self.inputContourName.data))

        imagecpy = self.inputImageName.data
        for cidx in contidx:
            cv2.drawContours(imagecpy, self.inputContourName.data, cidx, color=self.contourColor, thickness=1)
        self.outputImageName.data = imagecpy
