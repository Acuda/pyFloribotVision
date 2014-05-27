# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParameterBase.ui'
#
# Created: Wed May 14 10:33:13 2014
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
        ParameterBase.resize(584, 502)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ParameterBase)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(ParameterBase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaContent = QtGui.QWidget()
        self.scrollAreaContent.setGeometry(QtCore.QRect(0, 0, 562, 480))
        self.scrollAreaContent.setObjectName(_fromUtf8("scrollAreaContent"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaContent)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea.setWidget(self.scrollAreaContent)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(ParameterBase)
        QtCore.QMetaObject.connectSlotsByName(ParameterBase)

    def retranslateUi(self, ParameterBase):
        ParameterBase.setWindowTitle(_translate("ParameterBase", "Form", None))

