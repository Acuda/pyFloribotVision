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
from Ui_BoolParameter import Ui_BoolParameter as UiBase
import BaseParameterClasses as BPC

class BoolParameter(QtGui.QWidget, UiBase, BPC.ValueCallback):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.connect(self.checkBox, QtCore.SIGNAL('stateChanged(int)'), self.checkboxChanged)


    def checkboxChanged(self, value):
        if value == 2:
            self.doNotify(True)
        elif value == 0:
            self.doNotify(False)