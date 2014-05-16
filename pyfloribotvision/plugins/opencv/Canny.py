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
from pyfloribotvision.types.ImageType import ImageType

from .. BasePlugin import BasePlugin
import cv2

class Canny(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        IntType('threshold1', input=True),
        IntType('threshold2',  input=True),
    ]

    def __init__(self, **kwargs):
        super(Canny, self).__init__(**kwargs)

    def externalCall(self):
        image = self.inputImageName.data
        image = cv2.Canny(image, self.threshold1.data, self.threshold2.data)
        self.outputImageName.data = image
