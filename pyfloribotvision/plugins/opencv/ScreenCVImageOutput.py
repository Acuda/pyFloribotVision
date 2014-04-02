#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

import utils
from .. BaseModule import BaseModule
import cv2

class ScreenCVImageOutput(BaseModule):

    obligatoryConfigOptions = {'inputImageList': None}

    def __init__(self, **kwargs):
        super(ScreenCVImageOutput, self).__init__(**kwargs)

    def postOptActions(self):
        self.inputImageList = utils.configStrToList(self.inputImageList)

    def externalCall(self):
        for image in self.inputImageList:
            if image in self.ioContainer:
                cv2.imshow(image, self.ioContainer[image])
            else:


                print type(self.ioContainer)
                KeyList = self.ioContainer.keys()

                self.log.error('image <%s> not found in ioContainer - Keys: <%s>', image, KeyList)






