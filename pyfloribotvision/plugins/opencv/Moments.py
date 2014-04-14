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


class Moments(BaseModule):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputMomentListName', output=True),
    ]

    obligatoryConfigOptions = {'inputImageName': None, 'outputMomentListName': None}


    def __init__(self, **kwargs):
        super(Moments, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        momlist = cv2.moments(self.inputImageName.data, binaryImage=False)
        self.outputMomentListName.data = momlist
