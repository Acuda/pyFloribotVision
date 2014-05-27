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
from Ui_IntListParameter import Ui_IntListParameter as UiBase
import BaseParameterClasses as BPC
from IntListElementParameter import IntListElementParameter


class IntListParameter(QtGui.QWidget, UiBase, BPC.ValueUpdate, BPC.ValueCallback):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.activeParameters = dict()
        self.valueList = list()

    def setContent(self, valueList):
        self.valueList = valueList

        for ref, x in enumerate(valueList):

            ilelement = IntListElementParameter()
            ilelement.lineEdit.setText(str(x))

            ilelement.horizontalSlider.setMinimum(0)
            ilelement.horizontalSlider.setMaximum(300)
            ilelement.horizontalSlider.setSingleStep(1)
            ilelement.horizontalSlider.setPageStep(10)

            ilelement.horizontalSlider.setValue(x)

            self.formLayout.addWidget(ilelement)
            ilelement.registerNotify(self.widgetValueChanged)
            self.activeParameters[ilelement] = ref

    def widgetValueChanged(self, caller, value):
        for widget, data in self.activeParameters.items():
            if widget is caller:
                self.valueList[self.activeParameters[caller]] = int(value)
                self.doNotify(self.valueList)
                break
