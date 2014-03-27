#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from BaseModule import BaseModule
import cv2
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy as np
import logging


class DirectKinectSource(BaseModule):
    obligatoryConfigOptions = {}


    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


        self.initCam()

    def postOptActions(self):

        vid, _ = get_video()
        vid = np.array(vid)
        vid = cv2.cvtColor(vid, cv2.COLOR_RGB2BGR)

        self.ioContainer['vid'] = vid.copy()

        dep, _ = get_depth()
        fdep = np.float32(dep)
        fdep = 255 - np.uint8(cv2.normalize(fdep, fdep, 0, 255, cv2.NORM_MINMAX))

        self.ioContainer['dep3'] = fdep.copy()


    def initCam(self):
        pass
