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
from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.StringListType import StringListType
from .. BasePlugin import BasePlugin
import cv2
import logging
from utils import configStrToList


class CVContourConstraint(BasePlugin):

    configParameter = [
        NameType('inputContourName', input=True),
        NameType('outputContourIndexList', output=True),
        StringListType('contourFunctions'),
        StringType('resultPlaceholderName'),
        StringListType('contourConstraint'),
    ]

    def __init__(self, **kwargs):
        super(CVContourConstraint, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def preCyclicCall(self):
        assert len(self.contourFunctions.value) == len(self.contourConstraint.value)

        for k, fnc in enumerate(self.contourFunctions):
            if not hasattr(cv2, fnc):
                self.log.error('unknown contourFunction <%s>, deactivating module <%s>',
                               fnc, self.logicSectionName)
                self.activeModule = False

    def externalCall(self):
        cont = self.inputContourName.data
        contidx = range(len(cont))

        self.contourConstraint.data = list()
        for k, fnc in enumerate(self.contourFunctions):
            fnc = getattr(cv2, fnc)
            constraint = self.contourConstraint[k].replace(self.resultPlaceholderName.value, 'fnc(c)')
            self.contourConstraint.data.insert(k, constraint)

            self.log.debug('apply constraint <%s> for function <%s>', self.contourConstraint[k], fnc.__name__)
            contidx = [ck for ck, c in enumerate(cont) if ck in contidx and eval(self.contourConstraint.data[k])]

        self.outputContourIndexList.data = contidx






