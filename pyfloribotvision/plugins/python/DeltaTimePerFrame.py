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
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import time
import logging


class DeltaTimePerFrame(BasePlugin):

    configParameter = [
        BoolType('displayTime'),
        IntType('startFrame'),
        IntType('stopFrame'),
    ]

    def __init__(self, **kwargs):
        super(DeltaTimePerFrame, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        self.lastCallTime = time.time()
        self.timeList = list()
        self.frameCount = 1

    def externalCall(self):
        curtime = time.time()
        difftime = curtime - self.lastCallTime
        self.lastCallTime = curtime

        if self.startFrame.value <= self.frameCount <= self.stopFrame.value:
            self.timeList.append(difftime)

            if self.displayTime.value:
                print 'Frame: <%d>' % self.frameCount,
                self.printTime(difftime)
        self.frameCount += 1

        if self.frameCount == self.stopFrame:
            self.postCyclicCall()

    def postCyclicCall(self):
        midtime = float(sum(self.timeList)) / len(self.timeList)
        self.printTime(midtime)

    def printTime(self, time):
        print '%.2f' % (time*1.e3), 'ms', 1/time, 'Hz'