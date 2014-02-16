#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from .. BaseModule import BaseModule
import cv2
import logging
from utils import configStrToList


class CVContourConstraint(BaseModule):
    obligatoryConfigOptions = {'inputContourName': None, 'outputContourIndexList': None,
                               'contourFunctions': None, 'resultPlaceholderName': None, 'contourConstraint': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        self.contourFunctions = configStrToList(self.contourFunctions)
        self.contourConstraint = configStrToList(self.contourConstraint)
        assert len(self.contourFunctions) == len(self.contourConstraint)

        for k, fnc in enumerate(self.contourFunctions):
            if not hasattr(cv2, fnc):
                self.log.error('unknown contourFunction <%s>, deactivating module <%s>', fnc, self.logicSectionName)
                self.activeModule = False

    def externalCall(self):
        cont = self.ioContainer[self.inputContourName]
        contidx = range(len(cont))

        for k, fnc in enumerate(self.contourFunctions):
            fnc = getattr(cv2, fnc)
            self.contourConstraint[k] = self.contourConstraint[k].replace(self.resultPlaceholderName, 'fnc(c)')

            self.log.debug('apply constraint <%s> for function <%s>', self.contourConstraint[k], fnc.__name__)
            contidx = [ck for ck, c in enumerate(cont) if ck in contidx and eval(self.contourConstraint[k])]

        self.ioContainer[self.outputContourIndexList] = contidx






