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

class CVGaussBlur(BaseModule):

    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None,
                               'sigmaX': None, 'sigmaY': None, 'kSize': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

    def postOptActions(self):
        self.sigmaX = float(self.sigmaX.replace(' ', ''))
        self.sigmaY = float(self.sigmaY.replace(' ', ''))
        self.kSize = int(self.kSize.replace(' ', ''))

    def externalCall(self):
        image = self.ioContainer[self.inputImageName]
        image = cv2.GaussianBlur(image, (self.kSize, self.kSize), sigmaX=self.sigmaX, sigmaY=self.sigmaY)
        self.ioContainer[self.outputImageName] = image