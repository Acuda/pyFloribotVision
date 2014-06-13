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
from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.IntType import IntType

from .. BasePlugin import BasePlugin
import cv2
import numpy as np

class CircleDetector(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        NameType('inputContourName', input=True),
        IntType('thickness'),
        NameType('inputContourIndexListName', input=True),
        NameType('inputCalibrationData', input=True),
    ]

    def __init__(self, **kwargs):
        super(CircleDetector, self).__init__(**kwargs)
        self.scatter = np.zeros((300,300))


    def preCyclicCall(self):
        pass

    def externalCall(self):
        if self.inputContourIndexListName.data:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(self.inputContourName.data))
        image = self.inputImageName.data.copy()

        for cidx in contidx:
            cnt = self.inputContourName.data[cidx]
            mask = np.zeros(tuple(self.inputImageName.data.shape[:2]), np.uint8)
            cv2.drawContours(mask, self.inputContourName.data, -1, color=(250,250,50), thickness=-1)

            moments = cv2.moments(cnt)
            humoments = cv2.HuMoments(moments)


            try:
                centroid_x = moments['m10']/moments['m00']
                centroid_y = moments['m01']/moments['m00']
            except ZeroDivisionError:
                continue

            area = moments['m00']

            equi_diameter = np.sqrt(4*area/np.pi) * 1.1
            equi_radian = equi_diameter / 2.0



            #print self.inputCalibrationData.data
            xopt = self.inputCalibrationData.data[0,2]
            yopt = self.inputCalibrationData.data[1,2]



            # OPTICAL CENTER CROSSHAIR
            ##########################

            cv2.circle(image, (int(xopt), int(yopt)), 2, (100, 250, 100), -1)
            cv2.circle(image, (int(xopt), int(yopt)), 1, (250, 100, 100), -1)
            image[int(yopt), ..., 0:2] *= 0.5
            image[int(yopt), ...] *= 255.0 / image[int(yopt), ...].max()
            image[...,int(xopt), 0:2] *= 0.5
            image[...,int(xopt), 2] *= 255.0 / image[..., int(xopt), ...].max()


            B = equi_diameter * 0.0000031
            G = 0.0429
            b = 4.02e-3
            g = b/B*G
            gcorr = g + G/2

            color = (50, 250, 50)

            if humoments[0] > (1.64e-1) or humoments[0] < (1.59e-1) or equi_radian < 11:
                color = (50, 50, 250)
                #continue

            xpx = centroid_x - xopt
            xm = 0.0429 / equi_diameter * xpx

            ym = np.sqrt(gcorr**2 - xm**2)


            #print int(ym*100),int(xm*100)+100
            #self.scatter[int(ym*100)][int(xm*100)+100] += 0.1
            #cv2.imshow('scatter', cv2.pyrUp(self.scatter))
            #cv2.imwrite('data/scatterx.jpg', self.scatter)


            self.drawText(image, '%.2f'%xm, int(xopt), int(centroid_y), scale=1, color=(225, 225, 225))
            self.drawText(image, '%.2f'%ym, int(centroid_x), image.shape[0]-10, scale=1, color=(225, 225, 225))


            cv2.line(image, (int(centroid_x), int(centroid_y)), (int(xopt), int(centroid_y)), (200,50,50), 1)
            cv2.line(image, (int(centroid_x), int(centroid_y)), (int(centroid_x), image.shape[0]), (50,150,250), 1)

            cv2.circle(image, (int(centroid_x), int(centroid_y)), int(equi_radian), (200, 0, 0), 1)
            cv2.circle(image, (int(centroid_x), int(centroid_y)), 3, color=(255,50,50), thickness=-1)

            if True:
                #self.drawTextMarker(image, 'X: ' + str(round(centroid_x, 2)), centroid_x, centroid_y, equi_radian, 0, color)
                #self.drawTextMarker(image, 'Y: ' + str(round(centroid_y, 2)), centroid_x, centroid_y, equi_radian, 1, color)
                self.drawTextMarker(image, 'Radian: ' + str(round(equi_radian, 2)), centroid_x, centroid_y, equi_radian, 1, color)
                self.drawTextMarker(image, 'HM0' + ': %.2e' % humoments[0], centroid_x, centroid_y, equi_radian, 2, color)
                self.drawTextMarker(image, 'Distance' + ': %.2f' % gcorr + 'm', centroid_x, centroid_y, equi_radian, 3, color)

        cv2.imshow('xxx', image)

        #crop = image[125:450, 350:850]
        #crop = cv2.pyrUp(crop)
        #cv2.imshow('crop', crop)


    def drawTextMarker(self, image, text, xpos, ypos, radian, line, color=(225, 225, 225)):
        xofs = -35
        ystep = 15
        yofs = int(radian) + ystep * 4
        yofs *= -1
        self.drawText(image, text, int(xpos) + xofs, int(ypos) + yofs + ystep * line, 0.8, color)

    def drawText(self, image, text, xpos, ypos, scale=1, color=(225, 225, 225)):
        for i in range(3, 0, -1):
            if i < 2:
                cv2.putText(image, text, (xpos+i, ypos+i),
                            cv2.FONT_HERSHEY_PLAIN, scale, color)
            else:
                cv2.putText(image, text, (xpos+i, ypos+i),
                            cv2.FONT_HERSHEY_PLAIN, scale, (50, 50, 50))

