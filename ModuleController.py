#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

from ConfigController import *
import cv2
import logging
import logging.config
import time


class ModuleController(object):


    SECTIONNAME = 'GENERAL'

    def __init__(self, configController):
        logging.config.fileConfig('logging.conf')
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        assert isinstance(configController, ConfigController)
        assert isinstance(configController.rawConfig, ConfigParser)

        self.rawConfig = configController.rawConfig
        self.activeModules = list()
        self.ioContainer = dict()

        self.prepareGeneral()
        self.loadModules()

    def prepareGeneral(self):
        self.moduleList = self.rawConfig.get(self.SECTIONNAME, 'modules').replace(' ', '').replace('\n', '').split(',')
        print self.moduleList

    def loadModules(self):
        self.log.debug('=' * 30 + ' LOAD MODULES ' + '=' * 30)
        for sectionname in self.moduleList:
            if sectionname.startswith('!'):
                continue

            if self.rawConfig.has_section(sectionname) and self.rawConfig.has_option(sectionname, 'basemodule'):
                basemodule = self.rawConfig.get(sectionname, 'basemodule')

                dynmod = __import__('modules.' + basemodule, fromlist=[basemodule])
                dynclass = getattr(dynmod, basemodule)
                dynclassinstance = dynclass(rawConfig=self.rawConfig, logicSectionName=sectionname,
                                            ioContainer=self.ioContainer, moduleControllerInstance=self)
                self.activeModules.append(dynclassinstance)

    def runActiveModules(self):
        self.log.debug('=' * 30 + ' RUN ACTIVE MODULES ' + '=' * 30)
        runcycle = self.rawConfig.get(self.SECTIONNAME, 'runcycle').replace(' ', '')
        exitkey = self.rawConfig.get(self.SECTIONNAME, 'exitkey').replace(' ', '')

        while True:
            for k, module in enumerate(self.activeModules):
                if not module.activeModule:
                    self.log.debug('Skipping inactive Module <%s> for logical Section <%s>',
                                   module.__class__.__name__, module.logicSectionName)
                    continue

                self.log.debug('Calling Module <%s> for logical Section <%s>',
                               module.__class__.__name__, module.logicSectionName)
                module.externalCall()

            if runcycle == 'oneShoot':
                break

            if (cv2.waitKey(5) & 255) == ord(exitkey):
                break

        for k, module in enumerate(self.activeModules):
            if not module.activeModule:
                self.log.debug('Skipping inactive Module <%s> for logical Section <%s>',
                               module.__class__.__name__, module.logicSectionName)
                continue

            self.log.debug('Calling Module <%s> for logical Section <%s>',
                           module.__class__.__name__, module.logicSectionName)
            module.preOptActions()

if __name__ == "__main__":

    cc = ConfigController('default.conf')
    #cc.saveFile()


    ml = ModuleController(cc)
    ml.runActiveModules()