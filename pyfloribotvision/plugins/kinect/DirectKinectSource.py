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
from pyfloribotvision.types.BoolType import BoolType
from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import freenect
import numpy as np
import logging


class DirectKinectSource(BasePlugin):

    configParameter = [
        IntType('camId'),
        ImageType('outputImageName', output=True),
        ImageType('outputDepthImageName', output=True),
        NameType('outputDepthRawName', output=True),
        BoolType('reverseDepthVisualisation'),
    ]

    def __init__(self, **kwargs):
        super(DirectKinectSource, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        #try:
        self.log.debug('try to get image from cam')
        imageData, _ = freenect.sync_get_video(index=self.camId.value)
        depthDataRaw, _ = freenect.sync_get_depth()
        #except TypeError:
        #    self.log.error('asd')

        imageData = np.array(imageData)
        imageData = cv2.cvtColor(imageData, cv2.COLOR_RGB2BGR)

        self.outputImageName.data = imageData.copy()

        depthDataImage = np.float32(depthDataRaw)

        #depthDataImage = (depthDataImage)/2047*256
        #depthDataImage = np.uint8(depthDataImage)
        #depthDataImage = np.float32(depthDataImage) * 255 / 130
        depthDataImage = np.uint8(depthDataImage)

        #depthDataImage = depthDataImage * 255 / 130

        #depthDataImage = np.uint8(cv2.normalize(depthDataImage, depthDataImage, 0, 255, cv2.NORM_MINMAX))

        if self.reverseDepthVisualisation.value:
            depthDataImage = 255 - depthDataImage

        self.outputDepthImageName.data = depthDataImage.copy()
        self.outputDepthRawName.data = depthDataRaw.copy()

