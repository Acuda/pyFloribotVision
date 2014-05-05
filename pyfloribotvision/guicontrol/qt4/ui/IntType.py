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


class IntType(QtGui.QWidget, UiBase):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.callback = list()
        self.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.sliderChanged)

    def sliderChanged(self, value):
        self.lineEdit.setText(str(value))
        self.doNotify(value)

    def registerNotify(self, fnc):
        self.callback.append(fnc)

    def doNotify(self, value):
        for fnc in self.callback:
            fnc(self, value)

