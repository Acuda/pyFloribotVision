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

class CVGaussBlur(BaseModule):

    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)

    def externalCall(self):
        image = self.ioContainer[self.inputImageName]
        image = cv2.GaussianBlur(image, (3, 3), sigmaX=0, sigmaY=0.5)
        image = cv2.GaussianBlur(image, (3, 3), sigmaX=0, sigmaY=0.5)
        self.ioContainer[self.outputImageName] = image