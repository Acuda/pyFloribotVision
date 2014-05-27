# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntListElement.ui'
#
# Created: Tue May 13 09:59:51 2014
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

class Ui_IntListElement(object):
    def setupUi(self, IntListElement):
        IntListElement.setObjectName(_fromUtf8("IntListElement"))
        IntListElement.resize(577, 399)
        self.formLayout = QtGui.QFormLayout(IntListElement)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit = QtGui.QLineEdit(IntListElement)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalSlider = QtGui.QSlider(IntListElement)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.horizontalSlider)

        self.retranslateUi(IntListElement)
        QtCore.QMetaObject.connectSlotsByName(IntListElement)

    def retranslateUi(self, IntListElement):
        IntListElement.setWindowTitle(_translate("IntListElement", "Form", None))

