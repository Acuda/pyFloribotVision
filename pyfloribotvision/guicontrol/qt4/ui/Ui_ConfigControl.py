# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigControl.ui'
#
# Created: Thu Apr 10 14:59:25 2014
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
        ConfigControl.resize(400, 300)
        self.pushButton = QtGui.QPushButton(ConfigControl)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(ConfigControl)
        QtCore.QMetaObject.connectSlotsByName(ConfigControl)

    def retranslateUi(self, ConfigControl):
        ConfigControl.setWindowTitle(_translate("ConfigControl", "Form", None))
        self.pushButton.setText(_translate("ConfigControl", "PushButton", None))

