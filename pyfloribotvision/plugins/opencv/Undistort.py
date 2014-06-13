#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging
import pickle


class Undistort(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
        ImageType('outputImage', output=True),
        StringType('calibrationFile'),
        NameType('outputCalibrationData', output=True)
    ]

    def __init__(self, **kwargs):
        super(Undistort, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def preCyclicCall(self):
        with open(self.calibrationFile.value, 'rb') as f:
            self.camera_matrix = pickle.load(f)
            self.dist_coefs = pickle.load(f)

    def externalCall(self):

        image = self.inputImage.data

        if self.outputCalibrationData.data is None:
            self.outputCalibrationData.data, roi = cv2.getOptimalNewCameraMatrix(self.camera_matrix, self.dist_coefs, (image.shape[1], image.shape[0]), 0)

        image = cv2.undistort(image, self.camera_matrix, self.dist_coefs, None, self.outputCalibrationData.data)


        self.outputImage.data = image