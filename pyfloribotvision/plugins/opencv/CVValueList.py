#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.IntNestedListType import IntNestedListType
from pyfloribotvision.types.NameListType import NameListType
from .. BaseModule import BaseModule
import numpy as np
import logging

class CVValueList(BaseModule):

    configParameter = [
        IntNestedListType('inputValues'),
        NameListType('outputNames', output=True), StringType('runCycle'),
    ]

    obligatoryConfigOptions = {'inputValues': None, 'inputType': None, 'outputNames': None,
                               'runCycle': ['oneShoot', 'loop']}

    def __init__(self, **kwargs):
        super(CVValueList, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):

        self.outputNames.data = dict()
        converted = self.inputValues.getConvertedValue(np.array, np.uint8)

        self.log.debug('Value converted from <%s> to <%s>', self.inputValues.value, converted)
        self.log.debug('output values are: <%s>', self.outputNames.value)

        for key, value in enumerate(self.outputNames.value):
            self.log.debug('setting data dict with key <%s> to value <%s>', value, converted[key])
            self.outputNames.setDataValue(value, converted[key])
