#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from BaseModule import BaseModule
import cv2
import logging
from utils import *


class CVDrawContours(BaseModule):
    """
    if inputContourIndexListName is empty, then draw all contours
    """

    obligatoryConfigOptions = {'inputImageName': None, 'outputImageName': None,
                               'inputContourName': None, 'inputContourIndexListName': None, 'contourColor': None}

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

    def postOptActions(self):
        self.contourColor = map(int, configStrToList(self.contourColor))[::-1]

    def externalCall(self):
        cont = self.ioContainer[self.inputContourName]

        if self.inputContourIndexListName in self.ioContainer:
            contidx = self.ioContainer[self.inputContourIndexListName]
        else:
            contidx = range(len(cont))

        image = self.ioContainer[self.inputImageName]
        for cidx in contidx:
            cv2.drawContours(image, cont, cidx, color=self.contourColor)
