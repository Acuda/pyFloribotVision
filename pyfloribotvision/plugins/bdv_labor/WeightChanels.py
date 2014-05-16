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
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.IntType import IntType

from .. BasePlugin import BasePlugin
import cv2
import numpy as np

class WeightChanels(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        ImageType('outputImageName', output=True),
        IntType('ofs'),
    ]

    def __init__(self, **kwargs):
        super(WeightChanels, self).__init__(**kwargs)


    def preCyclicCall(self):
        pass

    def externalCall(self):

        hlut = np.sin(np.linspace(0, np.pi, 31))
        hblk = np.zeros(180-hlut.size, np.float32)
        hlut = np.concatenate((hlut, hblk))
        self.hlut = np.roll(hlut, self.ofs.value)

        flut = np.sin(np.linspace(0, np.pi*0.5, 256))*255
        fblk = np.zeros(256-flut.size, np.float32)
        self.flut = np.concatenate((flut, fblk))

        tflut = np.sin(np.linspace(0, np.pi*0.8, 256))*255
        tfblk = np.zeros(256-tflut.size, np.float32)
        self.tflut = np.concatenate((tflut, tfblk))

        image = self.inputImageName.data


        image = np.array(self.hlut[image[:, :, 0]] * \
            (0.2 * self.tflut[image[:, :, 1]] +
             0.8 * self.flut[image[:, :, 2]]), np.uint8)

        self.outputImageName.data = image



