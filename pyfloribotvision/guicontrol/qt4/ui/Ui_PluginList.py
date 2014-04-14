# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PluginList.ui'
#
# Created: Thu Apr 10 15:58:32 2014
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

class Ui_PluginList(object):
    def setupUi(self, PluginList):
        PluginList.setObjectName(_fromUtf8("PluginList"))
        PluginList.resize(400, 456)
        self.verticalLayout = QtGui.QVBoxLayout(PluginList)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(PluginList)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.btnUpdate = QtGui.QPushButton(PluginList)
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.verticalLayout.addWidget(self.btnUpdate)

        self.retranslateUi(PluginList)
        QtCore.QMetaObject.connectSlotsByName(PluginList)

    def retranslateUi(self, PluginList):
        PluginList.setWindowTitle(_translate("PluginList", "Form", None))
        self.btnUpdate.setText(_translate("PluginList", "PushButton", None))

