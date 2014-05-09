#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.



import cv2
from PyQt4 import QtGui
from PyQt4 import QtCore
from Ui_ImageParameter import Ui_ImageParameter as UiBase


class ImageParameter(QtGui.QWidget, UiBase):

    def __init__(self, **kwargs):
        QtGui.QWidget.__init__(self, **kwargs)
        self.setupUi(self)

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.updateImage)

        self._showImage = False
        self.btnToggleImage.clicked.connect(self.toggleShowImage)

    def toggleShowImage(self):
        self._showImage = not self._showImage
        if self._showImage:
            self.btnToggleImage.setText('HIDE')
            self._timer.start(200)
            self.videoFrame.setEnabled(True)
        else:
            self.btnToggleImage.setText('SHOW')
            self._timer.stop()



    def updateImage(self):
        self.videoFrame.setPixmap(self.convertImage())
        #self.videoFrame.setScaledContents(True)
        self.update()

    def convertImage(self):

        #print self.parameter.data
        frame = self.parameter.data.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width = frame.shape[:2]

        self.videoFrame.setMaximumHeight(height)
        #self.videoFrame.setGeometry(height=height)

        img = QtGui.QImage(frame, width, height, QtGui.QImage.Format_RGB888)
        img = QtGui.QPixmap.fromImage(img)
        return img