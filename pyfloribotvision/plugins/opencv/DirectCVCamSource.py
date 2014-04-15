#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.IntType import IntType
from .. BaseModule import BaseModule
import cv2
import logging
from cv2 import cv

class DirectCVCamSource(BaseModule):

    configParameter = [
        NameType('outputImageName', output=True),
        IntType('camId'), IntType('frameWidth'), IntType('frameHeight'),
    ]

    def __init__(self, **kwargs):
        super(DirectCVCamSource, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.initCam()

    def postOptActions(self):
        pass

    def initCam(self):
        self.cam = cv2.VideoCapture(self.camId.value)
        if self.frameWidth > 0:
            self.cam.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.frameWidth.value)
        if self.frameHeight > 0:
            self.cam.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.frameHeight.value)

    def timeBypassActions(self):
        self.cam.read()

    def externalCall(self):
        i, image = self.cam.read()
        self.ioContainer[self.outputImageName] = image.copy()
        self.outputImageName.data = image.copy()





