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
from manager.ContextManager import ContextManager

class PyFloribotVision(object):

    RELATIVE_PREFIX = '../'

    def __init__(self, configFile, loggingConfig, relativePath=True):
        if relativePath:
            configFile = PyFloribotVision.RELATIVE_PREFIX + configFile
            loggingConfig = PyFloribotVision.RELATIVE_PREFIX + loggingConfig

        self.configFile = configFile
        self.loggingConfig = loggingConfig
        self._context = None

        self.checkConfigExist()

        self.initApplicationContext()

    def checkConfigExist(self):
        with open(self.configFile) as fc, open(self.loggingConfig) as fl:
            fc.readline()
            fl.readline()

    def initApplicationContext(self):
        self._context = ContextManager()
        self._context.initContext(self.configFile, self.loggingConfig)









def main(name, argv):

    defaultConfigFile = 'config/default.conf'
    defaultLoggingConfig = 'config/logging.conf'
    relativePath = True

    # ToDo: real helptext..
    helptext = """%s
    FOO
    Bar
    """ % (name)

    helptext = '\n'.join([x.strip() for x in helptext.splitlines()])

    try:
        opts, args = getopt.getopt(argv, 'hc:l:', ['configfile=', 'loggingfile='])
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

    # Todo: check for a better way or abstraction
    try:
        PyFloribotVision(defaultConfigFile, defaultLoggingConfig, relativePath)
    except IOError as e:
        print(e)



if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])
