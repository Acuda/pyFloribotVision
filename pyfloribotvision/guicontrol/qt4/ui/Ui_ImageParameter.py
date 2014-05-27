# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageParameter.ui'
#
# Created: Thu May  8 19:19:41 2014
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
        ImageParameter.resize(424, 300)
        self.formLayout = QtGui.QFormLayout(ImageParameter)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(ImageParameter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(ImageParameter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.frame = QtGui.QFrame(ImageParameter)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnToggleImage = QtGui.QPushButton(self.frame)
        self.btnToggleImage.setObjectName(_fromUtf8("btnToggleImage"))
        self.horizontalLayout.addWidget(self.btnToggleImage)
        self.btnCloseImage = QtGui.QPushButton(self.frame)
        self.btnCloseImage.setEnabled(False)
        self.btnCloseImage.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.btnCloseImage)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.frame)
        self.videoFrame = QtGui.QLabel(ImageParameter)
        self.videoFrame.setEnabled(True)
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.videoFrame)

        self.retranslateUi(ImageParameter)
        QtCore.QMetaObject.connectSlotsByName(ImageParameter)

    def retranslateUi(self, ImageParameter):
        ImageParameter.setWindowTitle(_translate("ImageParameter", "Form", None))
        self.label.setText(_translate("ImageParameter", "TextLabel", None))
        self.btnToggleImage.setText(_translate("ImageParameter", "PLAY", None))
        self.btnCloseImage.setText(_translate("ImageParameter", "CLOSE", None))
        self.videoFrame.setText(_translate("ImageParameter", "NO IMAGE", None))

