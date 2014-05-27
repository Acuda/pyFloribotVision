# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BoolParameter.ui'
#
# Created: Mon May 12 23:39:55 2014
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

class Ui_BoolParameter(object):
    def setupUi(self, BoolParameter):
        BoolParameter.setObjectName(_fromUtf8("BoolParameter"))
        BoolParameter.resize(577, 399)
        self.formLayout = QtGui.QFormLayout(BoolParameter)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(BoolParameter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.checkBox = QtGui.QCheckBox(BoolParameter)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox)

        self.retranslateUi(BoolParameter)
        QtCore.QMetaObject.connectSlotsByName(BoolParameter)

    def retranslateUi(self, BoolParameter):
        BoolParameter.setWindowTitle(_translate("BoolParameter", "Form", None))
        self.label.setText(_translate("BoolParameter", "TextLabel", None))
        self.checkBox.setText(_translate("BoolParameter", "", None))

