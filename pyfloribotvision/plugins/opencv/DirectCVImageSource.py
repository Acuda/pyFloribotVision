#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.NameType import NameType
from .. BaseModule import BaseModule
import cv2
import logging


class DirectCVImageSource(BaseModule):

    configParameter = [
        StringType('inputImageFile'),
        NameType('outputImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(DirectCVImageSource, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        image = cv2.imread(self.inputImageFile.value)
        self.outputImageName.data = image.copy()