#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringListType import StringListType
from .. BasePlugin import BasePlugin
import cv2

class ScreenCVImageOutput(BasePlugin):

    configParameter = [
        StringListType('inputImageList', input=True),
    ]

    def __init__(self, **kwargs):
        super(ScreenCVImageOutput, self).__init__(**kwargs)

    def externalCall(self):
        for imagename, image in self.inputImageList.data.items():
            cv2.imshow(imagename, image)






