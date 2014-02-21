#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from __future__ import print_function
import getopt
import sys
from pyfloribotvision.manager.ContextManager import ContextManager
import cProfile

class PyFloribotVision(object):
    """Application-Startup handling Startup-Parameters"""

    def __init__(self, configFile, loggingConfig, relativePath=True):
        """Object initialization

        Arguments:
        configFile -- path to the plugin config
        loggingConfig -- path to the logging config
        relativePath -- if given paths not relative this should be set to False (default True)
        """

        self.relativePathPrefix = ''
        pluginprefix = '.'.join(__name__.split('.')[:-1])
        print('NAME',__name__)
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

        Arguments:
        pluginprefix -- plugins should be relative under ./plugins if class invoked trough a
            startup-script or another application, the prefix have to point into the package where
            the plugin-package could be find.
        """
        self._context = ContextManager()
        self._context.initContext(self.configFile, self.loggingConfig, pluginprefix)

    def executeApplicationContext(self):
        """execute configured behavior (invoke plugin methods)"""
        self._context.executeContext()



def main(name, argv):
    """Startup entry point, parsing commandline parameter"""
    print('enter main')
    global defaultConfigFile
    defaultConfigFile = 'config/default.conf'

    global defaultLoggingConfig
    defaultLoggingConfig = 'config/logging.conf'

    global relativePath
    relativePath = True
    profileExec = False

    # ToDo: real helptext..
    helptext = """%s
    """ % name

    helptext = '\n'.join([x.strip() for x in helptext.splitlines()])

    try:
        opts, args = getopt.getopt(argv, 'hr:c:l:', ['configfile=', 'loggingfile='])
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

    try:
        pfv = PyFloribotVision(defaultConfigFile, defaultLoggingConfig, relativePath)
        pfv.executeApplicationContext()
    except IOError as e:
        print(e)

if __name__ == "__main__":
    """Passtrougth if File was directly executed"""
    main(sys.argv[0], sys.argv[1:])
