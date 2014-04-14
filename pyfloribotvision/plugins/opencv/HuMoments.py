#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.IntListType import IntListType
from ..BaseModule import BaseModule
import cv2
import logging


class HuMoments(BaseModule):

    configParameter = [
        NameType('inputMomentListName', input=True),
        NameType('outputHuMomentListName', output=True),
    ]

    obligatoryConfigOptions = {'inputMomentListName': None, 'outputHuMomentListName': None}

    def __init__(self, **kwargs):
        super(HuMoments, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        humomlist = cv2.HuMoments(self.inputMomentListName.data)
        self.outputHuMomentListName.data = list(humomlist.reshape(1, -1)[0])

