#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.IntType import IntType
from pyfloribotvision.types.StringListType import StringListType
from .. BasePlugin import BasePlugin
from pyfloribotvision.manager.ContextManager import ContextManager
import cv2
import numpy as np
import logging
import pickle


class WaitKey(BasePlugin):

    configParameter = [
        IntType('waitTime'),
        StringListType('keyList'),
        StringListType('functionList'),
    ]

    def __init__(self, **kwargs):
        super(WaitKey, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')
        self.cm = ContextManager()

    def preCyclicCall(self):
        self.pm = self.cm.processManager

    def timeBypassActions(self):
        self.checkKey()

    def externalCall(self):
        self.checkKey()

    def checkKey(self):
        key = (cv2.waitKey(self.waitTime.value)&255)
        chkey =  chr(key)
        if chkey in self.keyList:
            for k, v in enumerate(self.keyList.value):
                if chkey is v:
                    fnc = getattr(self, self.functionList[k])
                    fnc()

    def stateHold(self):
        self.pm.changeState(self.pm.STATE_HOLD)
        print 'HOLD'

    def stateQuit(self):
        self.pm.changeState(self.pm.STATE_QUIT)
        print 'QUIT'

    def stateRun(self):
        self.pm.changeState(self.pm.STATE_RUN)
        print 'RUN'

