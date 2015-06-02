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
from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging
import pickle



class TestPlugin(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
    ]

    def __init__(self, **kwargs):
        super(TestPlugin, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):

        image = self.inputImage.data
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        hsv = cv2.pyrDown(hsv)


        hsv = cv2.pyrDown(hsv)
        hsv = cv2.pyrDown(hsv)



        green1 = hsv[...,0] < 33
        green2 = hsv[...,0] > 36

        hsv[...] = 255

        hsv[green1] = 0
        hsv[green2] = 0

        #se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        #hsv[...,2] = cv2.morphologyEx(hsv[...,2], cv2.MORPH_OPEN, se)




        se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
        hsv[...,2] = cv2.morphologyEx(hsv[...,2], cv2.MORPH_CLOSE, se)

        hsv = cv2.pyrUp(hsv)





        '''
        gray = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(gray,cv2.COLOR_BGR2HSV)
        edges = cv2.Canny(gray,100,50,apertureSize = 3)

        cv2.imshow('AR', edges)

        lines = cv2.HoughLines(edges,1,np.pi/180,100)

        if lines is not None:
            for rho,theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

                cv2.line(hsv,(x1,y1),(x2,y2),(0,0,255),2)

        '''




        hsv = cv2.pyrUp(hsv)
        hsv = cv2.pyrUp(hsv)



        image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

        th, thimagexx = cv2.threshold(gray, 1, 255, 0)
        cv2.imshow('thimagexx', thimagexx)

        cont, h = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        #image = cv2.pyrUp(image)
        #image = cv2.pyrUp(image)


        cv2.drawContours(image, cont, -1, (0,0,255))


        cv2.imshow('FOO', image)