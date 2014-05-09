#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


class ValueUpdate(object):

    def updateValue(self, value, dstFnc, convertFnc, preConvertFnc=None, postConvertFnc=None, **kwargs):
        try:
            if preConvertFnc is not None:
                value = preConvertFnc(value, **kwargs)

            cvalue = convertFnc(value)

            if postConvertFnc is not None:
                cvalue = postConvertFnc(cvalue, **kwargs)

            dstFnc(cvalue)
            self.doNotify(value)
        except ValueError as ex:
            raise ex

class ValueCallback(object):

    def createCallbackListIfNotExist(self):
        if not hasattr(self, 'callbackList'):
            self.callbackList = list()

    def registerNotify(self, fnc):
        self.createCallbackListIfNotExist()
        self.callbackList.append(fnc)

    def doNotify(self, value):
        self.createCallbackListIfNotExist()
        for fnc in self.callbackList:
            fnc(self, value)
