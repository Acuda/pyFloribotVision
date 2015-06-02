#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


import getopt
import sys
from pyfloribotvision.manager.ContextManager import ContextManager

class PyFloribotVision(object):
    """Application-Startup handling Startup-Parameters"""

    def __init__(self, configFile, loggingConfig, relativePath=True):
        """Object initialization

        :param configFile: path to the plugin config
        :param loggingConfig: path to the logging config
        :param relativePath: if given paths not relative this should be set to False
            (default ``True``)
        """

        self.relativePathPrefix = ''
        pluginprefix = '.'.join(__name__.split('.')[:-1])
        if __name__ == '__main__':
            self.relativePathPrefix = '../'
            pluginprefix = ''

        if relativePath:
            configFile = self.relativePathPrefix + configFile
            loggingConfig = self.relativePathPrefix + loggingConfig

        self.configFile = configFile
        self.loggingConfig = loggingConfig
        self._context = None

        self.checkConfigExist()

        self.initApplicationContext(pluginprefix)

    def checkConfigExist(self):
        """checks if config files are exists and readable"""
        with open(self.configFile) as fc, open(self.loggingConfig) as fl:
            fc.readline()
            fl.readline()

    def initApplicationContext(self, pluginprefix):
        """initializes the application context

        :param pluginprefix: plugins should be relative under ./plugins if class
            invoked trough a startup-script or another application, the prefix have
            to point into the package where the plugin-package could be found
        """
        self._context = ContextManager()
        self._context.initContext(self.configFile, self.loggingConfig, pluginprefix)

    def executeApplicationContext(self):
        """execute configured behavior (invoke plugin methods)"""
        self._context.executeContext()



def main(name, argv):
    """Startup entry point, parsing commandline parameter

    :param name: Name of the script which was executed
    :param argv: the list of command line arguments passed to the Python script
    """
    global defaultConfigFile
    defaultConfigFile = 'config/default.conf'

    global defaultLoggingConfig
    defaultLoggingConfig = 'config/logging.conf'

    global relativePath
    relativePath = True
    profileExec = False

    # ToDo: real helptext..
    helptext = """%s [-c configuration-file [-l logging-configuration [-flags]]]
    """ % name

    helptext = '\n'.join([x.strip() for x in helptext.splitlines()])

    if '--' in argv:
        argv.remove('--')

    try:
        opts, args = getopt.getopt(argv, 'hgr:c:l:', ['configfile=', 'loggingfile='])
    except getopt.GetoptError:
        print(helptext)
        sys.exit(2)


    for opt, arg in opts:
        if opt == '-h':
            print(helptext)
            sys.exit(2)
        elif opt in ("-c", "--configfile"):
            defaultConfigFile = arg
        elif opt in ("-l", "--loggingfile"):
            defaultLoggingConfig = arg
        elif opt in ("-r", "--relativepath"):
            relativePath = bool(arg)
        elif opt in ("-g"):
            from PyQt4 import QtGui
            from pyfloribotvision.guicontrol.qt4.ui.MainWindow import MainWindow
            app = QtGui.QApplication(sys.argv)
            mainWindow = MainWindow()
            mainWindow.show()

    try:
        pfv = PyFloribotVision(defaultConfigFile, defaultLoggingConfig, relativePath)
        pfv.executeApplicationContext()
    except IOError as e:
        print(e)

if __name__ == "__main__":
    """Passtrougth if File was directly executed"""
    main(sys.argv[0], sys.argv[1:])
