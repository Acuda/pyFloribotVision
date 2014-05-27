# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StringParameter.ui'
#
# Created: Fri May  9 14:07:43 2014
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


class Ui_StringParameter(object):
    def setupUi(self, StringParameter):
        StringParameter.setObjectName(_fromUtf8("StringParameter"))
        StringParameter.resize(577, 399)
        self.formLayout = QtGui.QFormLayout(StringParameter)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(StringParameter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(StringParameter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)

        self.retranslateUi(StringParameter)
        QtCore.QMetaObject.connectSlotsByName(StringParameter)

    def retranslateUi(self, StringParameter):
        StringParameter.setWindowTitle(_translate("StringType", "Form", None))
        self.label.setText(_translate("StringType", "TextLabel", None))

