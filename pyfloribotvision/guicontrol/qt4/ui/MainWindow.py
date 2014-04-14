#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from PyQt4 import QtGui
from Ui_MainWindow import Ui_MainWindow as UiBase
#from ConfigControl import ConfigControl
from PluginList import PluginList
from PyQt4 import QtCore
from pyfloribotvision.manager.ContextManager import ContextManager

class MainWindow(QtGui.QMainWindow, UiBase):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        css = ''
        with open('./config/dark.css', 'r') as f:
            css = ' '.join(f.readlines())
        self.setStyleSheet(css)

        self.textEdit = QtGui.QTextEdit()
        self.tab1Content.addWidget(self.textEdit)

        self.pluginList = PluginList()
        self.tab1Content.addWidget(self.pluginList)

        self.connect(self.pluginList.btnUpdate, QtCore.SIGNAL('clicked()'), self.loadList)
        self.connect(self.pluginList.listWidget, QtCore.SIGNAL('itemClicked(QListWidgetItem*)'), self.itemClicked)

        self.cm = ContextManager()


    def loadList(self):
        self.conf = self.cm.configController.getConfig()
        for x in self.conf:
            self.pluginList.listWidget.addItem(x)

    def itemClicked(self, item):
        assert isinstance(item, QtGui.QListWidgetItem)
        secconf = self.conf[str(item.text())]
        self.textEdit.setText(str(secconf))







