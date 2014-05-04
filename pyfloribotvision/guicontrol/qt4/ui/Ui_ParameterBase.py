# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParameterBase.ui'
#
# Created: Tue Apr 15 10:29:36 2014
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

class Ui_ParameterBase(object):
    def setupUi(self, ParameterBase):
        ParameterBase.setObjectName(_fromUtf8("ParameterBase"))
        ParameterBase.resize(336, 43)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ParameterBase)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ParameterBase)
        QtCore.QMetaObject.connectSlotsByName(ParameterBase)

    def retranslateUi(self, ParameterBase):
        ParameterBase.setWindowTitle(_translate("ParameterBase", "Form", None))

