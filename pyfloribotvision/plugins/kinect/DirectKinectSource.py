#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from .. BasePlugin import BasePlugin
import cv2
import freenect
import numpy as np
import logging


class DirectKinectSource(BasePlugin):
    obligatoryConfigOptions = {'camId': None, 'outputImageName': None, 'outputDepthImageName': None,
                               'outputDepthRawName': None, 'reverseDepthVisualisation': None}

    def __init__(self, **kwargs):
        super(DirectKinectSource, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        #from config
        self.reverseDepthVisualisation = self.reverseDepthVisualisation == str(True)
        self.camId = int(self.camId)

    def externalCall(self):
        #try:
        imageData, _ = freenect.sync_get_video(index=self.camId)
        depthDataRaw, _ = freenect.sync_get_depth()
        #except TypeError:
        #    self.log.error('asd')

        imageData = np.array(imageData)
        imageData = cv2.cvtColor(imageData, cv2.COLOR_RGB2BGR)

        self.ioContainer[self.outputImageName] = imageData.copy()

        depthDataImage = np.float32(depthDataRaw)



        #depthDataImage = (depthDataImage)/2047*256
        #depthDataImage = np.uint8(depthDataImage)
        #depthDataImage = np.float32(depthDataImage) * 255 / 130
        depthDataImage = np.uint8(depthDataImage)

        #depthDataImage = depthDataImage * 255 / 130

        #depthDataImage = np.uint8(cv2.normalize(depthDataImage, depthDataImage, 0, 255, cv2.NORM_MINMAX))

        if self.reverseDepthVisualisation:
            depthDataImage = 255 - depthDataImage

        self.ioContainer[self.outputDepthImageName] = depthDataImage.copy()
        self.ioContainer[self.outputDepthRawName] = depthDataRaw.copy()

