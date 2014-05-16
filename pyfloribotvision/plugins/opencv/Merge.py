#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.ImageListType import ImageListType
from pyfloribotvision.types.ImageType import ImageType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging


class Merge(BasePlugin):

    configParameter = [
        ImageListType('inputImageList', input=True),
        ImageType('outputImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(Merge, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):

        mdata = tuple([self.inputImageList.data[x] for x in self.inputImageList])
        self.outputImageName.data = cv2.merge(mdata)

