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
from ConfigControl import ConfigControl
from PluginList import PluginList
from PyQt4 import QtCore
from pyfloribotvision.manager.ContextManager import ContextManager
from pyfloribotvision.types.BaseType import BaseType
from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.IntType import IntType
from pyfloribotvision.types.NameType import NameType

class MainWindow(QtGui.QMainWindow, UiBase):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.typeHandleList = self.initTypeHandleDict()

        css = ''
        with open('./config/dark.css', 'r') as f:
            css = ' '.join(f.readlines())
        self.setStyleSheet(css)

        self.cc = ConfigControl()
        self.tab1Content.addWidget(self.cc)

        self.cc.verticalLayout.addChildWidget(QtGui.QPushButton())
        self.cc.verticalLayout.addChildWidget(QtGui.QPushButton())

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
        print '-'*50
        #print secconf
        for k, v in secconf.items():
            print k,
            if issubclass(type(v), BaseType):
                vclass = v.__class__
                if vclass in self.typeHandleList:
                    self.typeHandleList[vclass](v)
                else:
                    print 'NOT IMPLEMENTED', type(v)
                #print v.__class__, StringType,

        self.textEdit.setText(str(secconf))


    def initTypeHandleDict(self):
        thl = dict()

        thl[StringType] = self.handleString
        thl[IntType] = self.handleIntType
        thl[FloatType] = self.handleFloatType
        thl[NameType] = self.handleName

        return thl


    def handleString(self, parameter):
        print 'handle invoked STRING-TYPE for name <%s> and parameter-value <%s>' % (parameter.name, str(parameter.value))

    def handleIntType(self, parameter):
        print 'handle invoked INT-TYPE for name <%s> and parameter-value <%s>' % (parameter.name, str(parameter.value))

    def handleName(self, parameter):
        print 'handle invoked NAME-TYPE for name <%s> and parameter-value <%s>' % (parameter.name, str(parameter.value))

    def handleFloatType(self, parameter):
        print 'handle invoked FLOAT-TYPE for name <%s> and parameter-value <%s>' % (parameter.name, str(parameter.value))
        if parameter.name == 'sigmaY' or parameter.name == 'sigmaX':
            if parameter.value == 50.0:
                parameter.value = 0.0
            else:
                parameter.value = 50.0



