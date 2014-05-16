#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.

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
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import logging
import cv2
import numpy as np


class Histogram(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        ImageType('outputImageName', output=True),
        IntType('scale'),
    ]

    def __init__(self, **kwargs):
        super(Histogram, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


        self.hsv_map = np.zeros((180, 256, 3), np.uint8)
        h, s = np.indices(self.hsv_map.shape[:2])
        self.hsv_map[:, :, 0] = h
        self.hsv_map[:, :, 1] = s
        self.hsv_map[:, :, 2] = 255
        self.hsv_map = cv2.cvtColor(self.hsv_map, cv2.COLOR_HSV2BGR)

    def externalCall(self):

        image = self.inputImageName.data
        image = cv2.pyrDown(image)

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        h = np.clip(h*0.005*self.scale.value, 0, 1)
        vis = self.hsv_map * h[:, :, np.newaxis] / 255.0

        vis = cv2.pyrUp(vis)

        colsub = (0.2, 0.6, 0.2)
        colmain = (0.3, 0.9, 0.3)

        blacksize = 5

        for i in range(10, 360, 10):
            cv2.line(vis, (0, i), (5, i), 0, blacksize)
            cv2.line(vis, (0, i), (5, i), colsub, 1)
        for i in range(30, 360, 30):
            cv2.line(vis, (0, i), (15, i), 0, blacksize)
            cv2.line(vis, (0, i), (15, i), colmain, 1)

        for i in range(20, 510, 20):
            cv2.line(vis, (i, 0), (i, 5), 0, blacksize)
            cv2.line(vis, (i, 0), (i, 5), colsub, 1)
        for i in range(100, 510, 100):
            cv2.line(vis, (i, 0), (i, 15), 0, blacksize)
            cv2.line(vis, (i, 0), (i, 15), colmain, 1)

        self.outputImageName.data = vis
