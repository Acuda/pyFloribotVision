#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.IntType import IntType
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.BoolType import BoolType
from pyfloribotvision.types.StringType import StringType
from .. BasePlugin import BasePlugin
import logging
import cv2
import numpy as np
import time
import pickle

class Calibrate(BasePlugin):

    configParameter = [
        ImageType('inputImage', input=True),
        ImageType('outputImage', output=True),
        IntType('visualTresholdLow'),
        IntType('gridX'),
        IntType('gridY'),
        IntType('dataPerGridCell'),
        IntType('successHue'),
        IntType('boardw'),
        IntType('boardh'),
        FloatType('delay'),
        StringType('outputFileName'),
        BoolType('syncCalculation'),
    ]

    def __init__(self, **kwargs):
        super(Calibrate, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.data = np.zeros((self.gridY.value, self.gridX.value), np.uint8)

        self.board_w = self.boardw.value
        self.board_h = self.boardh.value

        self.board_n = self.board_w * self.board_h
        self.board_sz = (self.board_w, self.board_h)  # size of board


        pattern_size = (self.board_w, self.board_h)
        self.pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
        self.pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
        #pattern_points *= cbsq


        self.obj_points = list()
        self.img_points = list()

        self.last_time = time.time()

        self.syncObj = None

        self.calculationDone = False
        self.calculationVisualisation = False

    def externalCall(self):


        waitForSync = False
        if self.syncCalculation.value:

            waitForSync = True

            if not self.syncObj:
                self.syncObj = StringType('syncSection')
                self.syncObj.value = self.sectionConfig['syncSection']
                self.syncObj.data = False
                self.sectionConfig['syncSection'] = self.syncObj


            syncObjOther = self.fullConfig[self.syncObj.value][self.syncObj.name]
            if isinstance(syncObjOther, StringType):
                waitForSync = not syncObjOther.data


            #print self.logicSectionName,

            #print self.logicSectionName, self.fullConfig[secObj.value]['foo']



        image = self.inputImage.data

        # PREPARE VISUALIZATION

        if self.data is None:
            self.data = np.zeros((self.gridY.value, self.gridX.value), np.uint8)

        hsv = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)

        hsv[..., 0] = 0
        hsv[...,1] = 255

        dark = hsv[...,2] < self.visualTresholdLow.value
        hsv[dark] = self.visualTresholdLow.value

        # DRAW VISUALIZATION

        totalx = image.shape[1]
        totaly = image.shape[0]
        xsize = totalx // self.gridX.value
        ysize = totaly // self.gridY.value

        for y, yline in enumerate(self.data):
            for x, value in enumerate(yline):
                hsv[ysize*y:ysize*(y+1), xsize*x:xsize*(x+1), 0] = value * int(self.successHue.value / self.dataPerGridCell.value)



        doCalculate = self.data.sum() >= (self.dataPerGridCell.value * self.data.size)


        # AQUIRE BOARD DATA
        isBoard = False
        waitForDelay = time.time() - self.last_time <= self.delay.value
        if not doCalculate and not waitForDelay:

            isBoard, boardData = cv2.findChessboardCorners(image, self.board_sz, self.board_n,
                                                           cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FILTER_QUADS)

            attachToList = False

            if isBoard:
                cv2.drawChessboardCorners(hsv, self.board_sz, boardData, 0)
                for point in boardData:
                    x, y = point[0]
                    if self.data[y//ysize][x//xsize] < self.dataPerGridCell.value:
                        self.data[y//ysize][x//xsize] += 1
                        attachToList = True
                    self.last_time = time.time()

            if attachToList:
                self.img_points.append(boardData.reshape(-1, 2))
                self.obj_points.append(self.pattern_points)


        # CALCULATE
        self.syncObj.data = doCalculate
        if doCalculate and not waitForSync and not self.calculationDone and self.calculationVisualisation:

            self.calculationDone = True

            rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(self.obj_points, self.img_points, (totalx, totaly))

            print '*'*100
            print self.logicSectionName
            print '*'*100
            print "RMS:", rms
            print "camera matrix:\n", camera_matrix
            print "distortion coefficients: ", dist_coefs.ravel()
            print '*'*100

            with open(self.outputFileName.value, 'wb') as f:
                pickle.dump(camera_matrix, f, -1)
                pickle.dump(dist_coefs, f, -1)
                pickle.dump(rms, f, -1)
                pickle.dump(rvecs, f, -1)
                pickle.dump(tvecs, f, -1)




        self.outputImage.data = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


        if doCalculate:
            if waitForSync:
                textStr = 'wait for sync'
            else:
                if not self.calculationDone:
                    textStr = 'calculating'
                    self.calculationVisualisation = True
                else:
                    textStr = 'done'
        else:
            if isBoard or waitForDelay:
                textStr = 'board found'
            else:
                textStr = 'searching board'


        drawText(self.outputImage.data, textStr, 50, 50, scale=2, thickness=3, bgthickness=3)



def drawText(image, text, xpos, ypos, scale=1, color=(225, 225, 225), thickness=3, bgthickness=1):
    for i in range(thickness+bgthickness, 0, -1):
        if i < thickness:
            cv2.putText(image, text, (xpos+i, ypos+i),
                        cv2.FONT_HERSHEY_PLAIN, scale, color)
        else:
            cv2.putText(image, text, (xpos+i, ypos+i),
                        cv2.FONT_HERSHEY_PLAIN, scale, (50, 50, 50))