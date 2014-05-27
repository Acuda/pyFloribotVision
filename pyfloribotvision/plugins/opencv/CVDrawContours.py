#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.IntListType import IntListType
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import logging
import numpy as np

class CVDrawContours(BasePlugin):
    """
    if inputContourIndexListName is empty, then draw all contours
    """

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True),
        NameType('inputContourName', input=True),
        IntType('thickness'),
        NameType('inputContourIndexListName', input=True),
        IntListType('contourColor'),
    ]

    def __init__(self, **kwargs):
        super(CVDrawContours, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        if self.inputContourIndexListName.data:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(self.inputContourName.data))

        imagecpy = self.inputImageName.data
        for cidx in contidx:
            cv2.drawContours(imagecpy, self.inputContourName.data, cidx, color=self.contourColor, thickness=self.thickness.value)
        self.outputImageName.data = imagecpy




        '''
        if self.inputImageName.value == 'narf':
            shape = self.inputImageName.data.shape
            shape = list(shape)
            shape.append(3)
            shape = tuple(shape)
            foo = np.zeros(shape)

            for cidx in contidx:
                cv2.drawContours(foo, self.inputContourName.data, cidx, color=(100,100,100), thickness=1)

                center, radius = cv2.minEnclosingCircle(self.inputContourName.data[cidx])
                cv2.circle(foo, (int(center[0]),int(center[1])), int(radius), (255,0,0), 1)

                hull = cv2.convexHull(self.inputContourName.data[cidx], returnPoints=False)
                defects = cv2.convexityDefects(self.inputContourName.data[cidx], hull)
                print '-'*100

                for i in range(defects.shape[0]):
                    print i, defects[i, 0],
                    s,e,f,d = defects[i, 0]
                    print s,e,f,d

                    start = tuple(self.inputContourName.data[cidx][s][0])
                    end = tuple(self.inputContourName.data[cidx][e][0])
                    far = tuple(self.inputContourName.data[cidx][f][0])
                    print 'start, end, far', start, end, far

                    cv2.line(foo,start,end,[0,255,0],1)
                    cv2.circle(foo,far,1,[0,0,255],1)



            crop = foo[250:450, 500:800].copy()
            crop = cv2.pyrUp(crop)
            cv2.imshow('crop', crop)
            cv2.imshow('xxx', foo)
            '''