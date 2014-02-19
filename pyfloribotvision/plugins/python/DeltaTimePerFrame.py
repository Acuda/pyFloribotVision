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
    obligatoryConfigOptions = {}


    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def postOptActions(self):
        curtime = time.time()
        self.lastCallTime = curtime
        self.lastBypassTime = curtime

    def externalCall(self):
        curtime = time.time()
        difftime = curtime - self.lastCallTime
        self.lastCallTime = curtime
        print '%.2f' % (difftime*1.e3),'ms', 1/difftime, 'Hz'
