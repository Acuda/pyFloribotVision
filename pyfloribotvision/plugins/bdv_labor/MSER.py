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
import math
import numpy as np


class MSER(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        ImageType('inputOrginalImageName', input=True),
        ImageType('outputImageName', output=True),
        ImageType('outputImageMask', output=True),
        ImageType('outputOrginalImageFilt', output=True),
        FloatType('maskScale'),
        IntType('minRadius'),
        IntType('maxRadius'),
    ]

    def __init__(self, **kwargs):
        super(MSER, self).__init__(**kwargs)


    def preCyclicCall(self):
        pass

    def externalCall(self):
        d_red = cv2.cv.RGB(200, 100, 100)
        l_red = cv2.cv.RGB(250, 200, 200)
        d_green = cv2.cv.RGB(100, 200, 100)
        l_green = cv2.cv.RGB(200, 250, 200)

        orig = self.inputOrginalImageName.data
        img = orig.copy()
        #img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = self.inputImageName.data

        detector = cv2.FeatureDetector_create('MSER')
        fs = detector.detect(img2)
        #print dir(detector)

        fs.sort(key=lambda x: -x.size)


        def supress(x):
                for f in fs:
                    distx = f.pt[0] - x.pt[0]
                    disty = f.pt[1] - x.pt[1]
                    dist = math.sqrt(distx*distx + disty*disty)
                    #print f.size/1.5
                    if (f.size > x.size) and (dist < f.size/2) \
                        :#or (f.size > self.maxRadius.value) or (f.size < self.minRadius.value):
                        #print dist, self.minRadius.value, self.maxRadius.value

                        return True

        sfs = [x for x in fs if not supress(x)]

        mask = np.zeros_like(img2)

        for f in sfs:
                cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(2), d_red, 1)
                cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(f.size/2), d_green, 1)
                cv2.circle(mask, (int(f.pt[0]), int(f.pt[1])), int(f.size/1.5*self.maskScale.value), 255, -1)

        h, w = orig.shape[:2]
        #vis = np.zeros((h, w*2+5), np.uint8)
        #vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
        #vis[:h, :w] = orig
        #vis[:h, w+5:w*2+5] = img

        filt = np.zeros_like(orig)

        cv2.merge((mask, mask, mask), filt)

        filt = cv2.bitwise_and(orig, filt)

        self.outputImageMask.data = mask
        self.outputImageName.data = img
        self.outputOrginalImageFilt.data = filt
