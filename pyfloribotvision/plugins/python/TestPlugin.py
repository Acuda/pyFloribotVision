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
from pyfloribotvision.types.BoolType import BoolType
from .. BasePlugin import BasePlugin
import cv2
import numpy as np
import logging
import pickle
import serial

class TestPlugin(BasePlugin):

    configParameter = [
        BoolType('doOutput'),
    ]

    def __init__(self, **kwargs):
        super(TestPlugin, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self.pf = open('data/gps4.pickle', 'wb')

        self.baudrate = 38400
        self.fio = '/dev/ttyUSB0'
        self.initSerial()

    def initSerial(self):
        self.ser = serial.Serial(self.fio, baudrate=self.baudrate)

    def getGeo(self):
        geo = self.ser.readline()
        return geo

    def printGeo(self):
        print self.getGeo()


    def externalCall(self):
        geo = self.getGeo()
        #pickle.dump(geo, self.pf, -1)
