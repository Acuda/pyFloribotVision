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
from pyfloribotvision.types.IntListType import IntListType
from .. BaseModule import BaseModule
#from BaseModule import BaseModule
import cv2
import numpy as np
import logging


class CVBitwiseOr(BaseModule):

    configParameter = [
        NameType('inputImageName1', input=True),
        NameType('inputImageName2', input=True),
        NameType('outputImageName', output=True),
    ]

    obligatoryConfigOptions = {'inputImageName1': None, 'inputImageName2': None,
                               'outputImageName': None}

    def __init__(self, **kwargs):
        super(CVBitwiseOr, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        image = np.zeros(self.inputImageName1.data.shape, np.uint8)
        cv2.bitwise_or(self.inputImageName1.data, self.inputImageName2.data, image)
        self.outputImageName.data = image