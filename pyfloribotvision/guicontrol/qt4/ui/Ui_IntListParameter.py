# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntListParameter.ui'
#
# Created: Tue May 13 18:51:13 2014
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

class Ui_IntListParameter(object):
    def setupUi(self, IntListParameter):
        IntListParameter.setObjectName(_fromUtf8("IntListParameter"))
        IntListParameter.resize(577, 399)
        self.verticalLayout = QtGui.QVBoxLayout(IntListParameter)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(IntListParameter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(IntListParameter)
        QtCore.QMetaObject.connectSlotsByName(IntListParameter)

    def retranslateUi(self, IntListParameter):
        IntListParameter.setWindowTitle(_translate("IntListParameter", "Form", None))
        self.groupBox.setTitle(_translate("IntListParameter", "GroupBox", None))

