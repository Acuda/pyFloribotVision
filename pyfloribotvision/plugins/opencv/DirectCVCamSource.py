#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import cv2
import logging
from cv2 import cv

class DirectCVCamSource(BaseModule):

    obligatoryConfigOptions = {'camId': None, 'outputImageName': None, 'frameWidth': None,
                               'frameHeight': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.initCam()

    def postOptActions(self):
        pass

    def initCam(self):
        self.frameWidth = float(self.frameWidth.replace(' ', ''))
        self.frameHeight = float(self.frameHeight.replace(' ', ''))

        self.cam = cv2.VideoCapture(self.camId)
        if self.frameWidth > 0:
            self.cam.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.frameWidth)
        if self.frameHeight > 0:
            self.cam.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.frameHeight)



    def timeBypassActions(self):
        self.cam.read()

    def postOptActions(self):
        self.camId = int(self.camId.replace(' ', ''))

    def externalCall(self):
        i, image = self.cam.read()
        self.ioContainer[self.outputImageName] = image.copy()





