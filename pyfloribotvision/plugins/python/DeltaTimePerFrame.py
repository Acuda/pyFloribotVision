#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import time
import logging


class DeltaTimePerFrame(BaseModule):
    obligatoryConfigOptions = {'displayTime': ['True', 'False'], 'startFrame': None, 'stopFrame': None}


    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def postOptActions(self):
        curtime = time.time()
        self.lastCallTime = curtime
        self.lastBypassTime = curtime
        self.timeList = list()
        self.frameCount = 1

        #from config
        self.displayTime = self.displayTime == str(True)
        self.stopFrame = int(self.stopFrame)
        self.startFrame = int(self.startFrame)


    def externalCall(self):
        curtime = time.time()
        difftime = curtime - self.lastCallTime
        self.lastCallTime = curtime

        if self.startFrame <= self.frameCount <= self.stopFrame:
            self.timeList.append(difftime)

            if self.displayTime:
                print 'Frame: <%d>' % self.frameCount,
                self.printTime(difftime)
        self.frameCount += 1

    def preOptActions(self):
        midtime = float(sum(self.timeList)) / len(self.timeList)
        self.printTime(midtime)

    def printTime(self, time):
        print '%.2f' % (time*1.e3), 'ms', 1/time, 'Hz'