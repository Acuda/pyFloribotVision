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

class CircleMarker(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        ImageType('outputImageName', output=True),
        IntType('ofs'),
    ]

    def __init__(self, **kwargs):
        super(CircleMarker, self).__init__(**kwargs)


    def preCyclicCall(self):
        pass

    def externalCall(self):
        pass



