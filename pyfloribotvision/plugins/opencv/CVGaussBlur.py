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
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.IntType import IntType

from .. BaseModule import BaseModule
import cv2

class CVGaussBlur(BaseModule):

    configParameter = [
        NameType('inputImageName', input=True), NameType('outputImageName', output=True),
        FloatType('sigmaX'), FloatType('sigmaY'),
        IntType('kSize'),
    ]

    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None,
                               'sigmaX': None, 'sigmaY': None, 'kSize': None}

    def __init__(self, **kwargs):
        super(CVGaussBlur, self).__init__(**kwargs)

    def externalCall(self):
        #image = self.ioContainer[self.inputImageName]
        image = self.inputImageName.data
        image = cv2.GaussianBlur(image, (self.kSize.value, self.kSize.value),
                                 sigmaX=self.sigmaX.value, sigmaY=self.sigmaY.value)
        self.outputImageName.data = image
        #self.ioContainer[self.outputImageName] = image
