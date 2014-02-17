#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

from BaseModule import BaseModule
import cv2
import logging

class DirectCVCamSource(BaseModule):

    obligatoryConfigOptions = {'camId': None, 'outputImageName': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.initCam()

    def initCam(self):
        self.cam = cv2.VideoCapture(self.camId)
        self.cam.set(3, 1280)
        self.cam.set(4, 1024)

    def timeBypassActions(self):
        self.cam.read()

    def postOptActions(self):
        self.camId = int(self.camId.replace(' ', ''))

    def externalCall(self):
        i, image = self.cam.read()
        self.ioContainer[self.outputImageName] = image.copy()





