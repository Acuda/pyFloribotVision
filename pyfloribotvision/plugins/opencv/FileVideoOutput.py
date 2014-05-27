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
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.NameType import NameType
from .. BasePlugin import BasePlugin
import cv2
import logging


class FileVideoOutput(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        StringType('outputVideoFile'),
        FloatType('fps'),
    ]

    def __init__(self, **kwargs):
        super(FileVideoOutput, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def preCyclicCall(self):
        self.fourcc = cv2.cv.FOURCC(*'XVID')

    def externalCall(self):
        image = self.inputImageName.data
        if self.outputVideoFile.data is None:
            self.outputVideoFile.data = cv2.VideoWriter(self.outputVideoFile.value,
                                                        self.fourcc, self.fps.value,
                                                        (image.shape[1],
                                                         image.shape[0]))
        self.outputVideoFile.data.write(image)


