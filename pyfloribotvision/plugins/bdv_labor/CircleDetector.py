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
    ]

    def __init__(self, **kwargs):
        super(CircleDetector, self).__init__(**kwargs)


    def preCyclicCall(self):
        pass

    def externalCall(self):
        if self.inputContourIndexListName.data:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(self.inputContourName.data))

        image = self.inputImageName.data.copy()

        #cv2.drawContours(foo, self.inputContourName.data, -1, color=(250,250,50), thickness=1)
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
            perimeter = cv2.arcLength(cnt, True)



            hull = cv2.convexHull(cnt)
            #cv2.drawContours(foo, [hull], 0, color=(50, 50, 200), thickness=1)
            hull_area = cv2.contourArea(hull)
            solidity = float(area)/hull_area

            ellipse = cv2.fitEllipse(cnt) if area > 5 else ((centroid_x, centroid_y), (0, 0), 0)

            equi_diameter = np.sqrt(4*area/np.pi)
            equi_radian = equi_diameter / 2.0

            x,y,w,h = cv2.boundingRect(cnt)
            aspect_ratio = float(w)/h

            mean_val = cv2.mean(image, mask=mask)

            color = (50, 250, 50)
            """
            if solidity < 0.89:
                color = (50, 50, 250)
                #continue

            if equi_radian < 10:
                color = (50, 200, 250)
                #continue

            if solidity < 0.9 and equi_radian < 10:
                color = (50, 250, 250)
                #continue
            """

            if humoments[0] > (1.64e-1):
                color = (50, 50, 250)
            if humoments[0] < (1.59e-1):
                color = (50, 200, 250)



            cv2.circle(image, (int(centroid_x), int(centroid_y)), int(equi_radian), (200, 0, 0), 1)
            cv2.circle(image, (int(centroid_x), int(centroid_y)), 3, color=(255,50,50), thickness=-1)
            #if ellipse:
                #cv2.ellipse(foo, ellipse, (0,255,0), 2)



            #elli = cv2.fitEllipse(cnt)
            #cv2.ellipse()
            #print elli


            if True:
                self.drawTextMarker(image, 'X: ' + str(round(centroid_x, 2)), centroid_x, centroid_y, equi_radian, 0, color)
                self.drawTextMarker(image, 'Y: ' + str(round(centroid_y, 2)), centroid_x, centroid_y, equi_radian, 1, color)
                self.drawTextMarker(image, 'Radian: ' + str(round(equi_radian, 2)), centroid_x, centroid_y, equi_radian, 2, color)
                self.drawTextMarker(image, 'HM0' + ': %.2e' % humoments[0], centroid_x, centroid_y, equi_radian, 3, color)
                #self.drawTextMarker(foo, str(round(100*solidity, 2))+'%', centroid_x, centroid_y, equi_radian, 4, color)
                #self.drawTextMarker(foo, 'Perimeter: ' + str(round(perimeter, 2)), centroid_x, centroid_y, equi_radian, 5, color)
                #self.drawTextMarker(foo, 'aspect_ratio : ' + str(round(aspect_ratio, 2)), centroid_x, centroid_y, equi_radian, 6, color)
                #self.drawTextMarker(foo, '##########', centroid_x, centroid_y, equi_radian, 6, (mean_val[0],mean_val[1],mean_val[2]))
            else:
                for i, hu in enumerate(humoments):
                    self.drawTextMarker(image, 'HM' + str(i) + ': %.3e' % humoments[i], centroid_x, centroid_y, equi_radian, i, color)

        cv2.imshow('xxx', image)



        crop = image[125:450, 350:850]
        crop = cv2.pyrUp(crop)
        cv2.imshow('crop', crop)


    def drawTextMarker(self, image, text, xpos, ypos, radian, line, color=(225, 225, 225)):
        xofs = -35
        ystep = 15
        yofs = int(radian) + ystep * 7
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

