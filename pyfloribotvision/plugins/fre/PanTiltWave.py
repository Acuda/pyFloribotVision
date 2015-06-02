#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.



from pyfloribotvision.types.BoolType import BoolType

from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import serial

class PanTiltWave(BasePlugin):

    configParameter = [
        BoolType('detected', input=True),
    ]

    def __init__(self, **kwargs):
        super(PanTiltWave, self).__init__(**kwargs)


        self.ser = serial.Serial('/dev/ttyUSB0')
        self.UPL = 1800
        self.LPL = -self.UPL

        self.UTL = 1800
        self.LTL = -self.UTL

        self.w(self.ser,'L')
        self.r(self.ser)


    def preCyclicCall(self):
        pass

    def externalCall(self):
        print self.detected.data

        if self.detected.data:
            self.TiltUp()
        else:
            self.TiltDown()


    def TiltUp(self):
        self.t(-1800)

    def TiltDown(self):
        self.t(0)

    
    def w(self, ser, msg):
        ser.write(msg + '\n')
        self.r(ser)

    def r(self, ser):
        if ser.readable():
            print ser.readline(),

    def p(self, pos):
        pos = self.checkPL(pos)
        self.w(ser, 'PP%d'%pos)

    def checkPL(self, pos):
        if pos > self.UPL:
            pos = self.UPL

        if pos < self.LPL:
            pos = self.LPL

        return pos

    def t(self, pos):
        pos = self.checkTL(pos)
        self.w(self.ser, 'TP%d'%pos)

    def checkTL(self, pos):
        if pos > self.UTL:
            pos = self.UTL

        if pos < self.LTL:
            pos = self.LTL

        return pos
    
