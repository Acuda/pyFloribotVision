# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageParameter.ui'
#
# Created: Mon May  5 22:25:18 2014
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

class Ui_ImageParameter(object):
    def setupUi(self, ImageParameter):
        ImageParameter.setObjectName(_fromUtf8("ImageParameter"))
        ImageParameter.resize(400, 300)
        self.formLayout = QtGui.QFormLayout(ImageParameter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(ImageParameter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(ImageParameter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.videoFrame = QtGui.QLabel(ImageParameter)
        self.videoFrame.setEnabled(False)
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.videoFrame)
        self.btnToggleImage = QtGui.QPushButton(ImageParameter)
        self.btnToggleImage.setObjectName(_fromUtf8("btnToggleImage"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.btnToggleImage)

        self.retranslateUi(ImageParameter)
        QtCore.QMetaObject.connectSlotsByName(ImageParameter)

    def retranslateUi(self, ImageParameter):
        ImageParameter.setWindowTitle(_translate("ImageParameter", "Form", None))
        self.label.setText(_translate("ImageParameter", "TextLabel", None))
        self.videoFrame.setText(_translate("ImageParameter", "NO IMAGE", None))
        self.btnToggleImage.setText(_translate("ImageParameter", "SHOW", None))

