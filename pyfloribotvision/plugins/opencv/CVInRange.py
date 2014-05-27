#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.ImageType import ImageType
from pyfloribotvision.types.NameListType import NameListType
from .. BasePlugin import BasePlugin
import cv2
import logging


class CVInRange(BasePlugin):

    configParameter = [
        ImageType('inputImageName', input=True),
        NameListType('cvValueListNames', input=True),
        NameListType('outputMaskListNames', output=True),
    ]

    def __init__(self, **kwargs):
        super(CVInRange, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def externalCall(self):
        self.log.debug('check parameter (dependecy) for cvValueListNames (name, value data): '
                       '<%s>  <%s>  <%s>', self.cvValueListNames.name, self.cvValueListNames.value,
                       self.cvValueListNames.data)

        stepsize = 2
        for i in range(len(self.cvValueListNames.value)/stepsize):
            minkey = self.cvValueListNames.value[(i * stepsize)]
            maxkey = self.cvValueListNames.value[(i * stepsize) + 1]
            minvalue = self.cvValueListNames.data[minkey]
            maxvalue = self.cvValueListNames.data[maxkey]

            self.log.debug('inRange action Nr. <%s> for inputImageName <%s> creating image <%s>',
                           i, self.inputImageName.value, self.outputMaskListNames.value[i])
            self.log.debug('checking lower border <%s> with <%s> up to upper border <%s> with <%s>',
                           minkey, minvalue, maxkey, maxvalue)

            imagebin = cv2.inRange(self.inputImageName.data, minvalue, maxvalue)
            self.outputMaskListNames.setDataValue(self.outputMaskListNames.value[i], imagebin)
