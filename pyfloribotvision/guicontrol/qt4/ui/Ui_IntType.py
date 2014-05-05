# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntType.ui'
#
# Created: Mon May  5 19:58:12 2014
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

class Ui_IntType(object):
    def setupUi(self, IntType):
        IntType.setObjectName(_fromUtf8("IntType"))
        IntType.resize(577, 399)
        self.formLayout = QtGui.QFormLayout(IntType)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(IntType)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(IntType)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalSlider = QtGui.QSlider(IntType)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.horizontalSlider)

        self.retranslateUi(IntType)
        QtCore.QMetaObject.connectSlotsByName(IntType)

    def retranslateUi(self, IntType):
        IntType.setWindowTitle(_translate("IntType", "Form", None))
        self.label.setText(_translate("IntType", "TextLabel", None))

