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
from pyfloribotvision.types.StringType import StringType
from .. BasePlugin import BasePlugin
import logging
import cv2
from cv2 import cv

class DirectVideoSource(BasePlugin):

    configParameter = [
        StringType('inputVideoFile'),
        ImageType('outputImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(DirectVideoSource, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        self.initVideo()

    def initVideo(self):
        self.inputVideoFile.data = cv2.VideoCapture(self.inputVideoFile.value)

    def externalCall(self):
        if self.inputVideoFile.data.isOpened():
            ret, image = self.inputVideoFile.data.read()
            if ret:
                self.outputImageName.data = image.copy()
            else:
                self.initVideo()




