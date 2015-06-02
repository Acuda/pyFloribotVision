#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.



from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.BoolType import BoolType
from pyfloribotvision.types.IntType import IntType
from pyfloribotvision.types.ImageType import ImageType

from .. BasePlugin import BasePlugin
import cv2
import numpy as np

class HoughCircles(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        StringType('circleData', output=True),
        IntType('dp', constraint=range(1,1000)),
        IntType('minDist', constraint=range(1,1000)),
        IntType('minRad', constraint=range(1,1000)),
        IntType('maxRad', constraint=range(1,1000)),
        IntType('threshold1', constraint=range(1,1000)),
        IntType('threshold2', constraint=range(1,1000)),
        ImageType('inputOrgImageName', input=True),
        BoolType('doDrawCircles'),
        ImageType('outputOrgCircleImageName', output=True),
        BoolType('doCannyOutput'),
        ImageType('outputCannyImageName', output=True),
    ]

    def __init__(self, **kwargs):
        super(HoughCircles, self).__init__(**kwargs)

    def externalCall(self):


        reslist = cv2.HoughCircles(self.inputImageName.data,
                                   cv2.cv.CV_HOUGH_GRADIENT,
                                   dp=self.dp.value,
                                   minDist=self.minDist.value,
                                   minRadius=self.minRad.value,
                                   maxRadius=self.maxRad.value,
                                   param1=self.threshold1.value,
                                   param2=self.threshold2.value)

        self.circleData.data = reslist

        if self.doCannyOutput.value:
            image = self.inputImageName.data
            canny = cv2.Canny(image, self.threshold1.value, self.threshold1.value//2)
            self.outputCannyImageName.data = canny



        if self.doDrawCircles.value:
            resvisimage = self.inputOrgImageName.data.copy()



            if reslist is not None and len(reslist):
                for x in reslist[0]:
                    corr = 5
                    mask = np.zeros(tuple(self.inputImageName.data.shape[:2]), np.uint8)
                    cv2.circle(mask, (x[0], x[1]), int(x[2]-corr), 255, -1)

                    mean_val = cv2.mean(self.inputOrgImageName.data, mask=mask)
                    mv = np.zeros((1, 1, 3), np.uint8)

                    mv[..., 0] = mean_val[0]
                    mv[..., 1] = mean_val[1]
                    mv[..., 2] = mean_val[2]

                    mv2 = cv2.cvtColor(mv, cv2.COLOR_BGR2HSV)

                    #cv2.circle(resvisimage, (x[0], x[1]), int(x[2]-corr), (mean_val[0],mean_val[1],mean_val[2]), -1)
                    self.drawText(resvisimage, str(mv2[0,0]), x[0]-40, x[1] - self.maxRad.value-4, 1)


                    if 28 > mv2[0,0,0] or mv2[0,0,0] > 32 or mv2[0,0,1] < 70 or mv2[0,0,2] < 150:
                        #continue
                        pass




                    cv2.circle(resvisimage, (x[0], x[1]), self.minRad.value, (100, 255, 100), 1)
                    cv2.circle(resvisimage, (x[0], x[1]), self.maxRad.value, (100, 100, 255), 1)
                    cv2.circle(resvisimage, (x[0], x[1]), self.minDist.value, (100, 100, 100), 1)
                    cv2.circle(resvisimage, (x[0], x[1]), x[2], (255, 100, 100), 2)
                    cv2.circle(resvisimage, (x[0], x[1]), 4, (50, 50, 50), -1)


            self.outputOrgCircleImageName.data = resvisimage



    def drawText(self, image, text, xpos, ypos, scale=1, color=(225, 225, 225)):
        xpos = int(xpos)
        ypos = int(ypos)
        for i in range(3, 0, -1):
            if i < 2:
                cv2.putText(image, text, (xpos+i, ypos+i),
                            cv2.FONT_HERSHEY_PLAIN, scale, color)
            else:
                cv2.putText(image, text, (xpos+i, ypos+i),
                            cv2.FONT_HERSHEY_PLAIN, scale, (50, 50, 50))

