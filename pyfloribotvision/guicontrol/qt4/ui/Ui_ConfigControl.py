# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigControl.ui'
#
# Created: Tue Apr 15 10:33:04 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConfigControl(object):
    def setupUi(self, ConfigControl):
        ConfigControl.setObjectName(_fromUtf8("ConfigControl"))
        ConfigControl.resize(582, 404)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigControl)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ConfigControl)
        QtCore.QMetaObject.connectSlotsByName(ConfigControl)

    def retranslateUi(self, ConfigControl):
        ConfigControl.setWindowTitle(_translate("ConfigControl", "Form", None))

