#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from PyQt4 import QtGui
from PyQt4 import QtCore
from Ui_IntType import Ui_IntType as UiBase
import BaseParameterClasses as BPC

class FloatParameter(QtGui.QWidget, UiBase, BPC.ValueUpdate, BPC.ValueCallback):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.scaleFactor = 10

        self.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.sliderChanged)
        self.connect(self.lineEdit, QtCore.SIGNAL('textChanged(QString)'),
                     self.lineEditChanged)

    def lineEditChanged(self, value):
        self.updateValue(value, self.horizontalSlider.setValue, convertFnc=float,
                         postConvertFnc=self.scaleValue,
                         scaleFactor=self.scaleFactor)

    def sliderChanged(self, value):
        self.updateValue(value, self.lineEdit.setText, str,
                         preConvertFnc=self.scaleValue,
                         scaleFactor=self.scaleFactor**-1)

    def scaleValue(self, value, scaleFactor=1):
        print type(value)
        return value * scaleFactor

