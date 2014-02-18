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



    def __init__(self, configFile, loggingConfig, relativePath=True):

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
        with open(self.configFile) as fc, open(self.loggingConfig) as fl:
            fc.readline()
            fl.readline()

    def initApplicationContext(self, pluginprefix):
        self._context = ContextManager()
        self._context.initContext(self.configFile, self.loggingConfig, pluginprefix)

    def executeApplicationContext(self):
        self._context.executeContext()




def profileExecStuff():
    pfv = PyFloribotVision(defaultConfigFile, defaultLoggingConfig, relativePath)
    pfv.executeApplicationContext()


def main(name, argv):
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
    FOO
    Bar
    """ % (name)

    helptext = '\n'.join([x.strip() for x in helptext.splitlines()])

    try:
        opts, args = getopt.getopt(argv, 'hpr:c:l:', ['configfile=', 'loggingfile='])
    except getopt.GetoptError:
        print(helptext)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helptext)
            sys.exit(2)
        elif opt == '-p':
            profileExec = True
        elif opt in ("-c", "--configfile"):
            defaultConfigFile = arg
        elif opt in ("-l", "--loggingfile"):
            defaultLoggingConfig = arg
        elif opt in ("-r", "--relativepath"):
            relativePath = bool(arg)

    print('sysops ok')

    # Todo: check for a better way or abstraction
    try:
        if not profileExec:
            print('propfile exec')
            pfv = PyFloribotVision(defaultConfigFile, defaultLoggingConfig, relativePath)
            pfv.executeApplicationContext()
        else:
            cProfile.run('profileExecStuff()')
    except IOError as e:
        print(e)



if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])
