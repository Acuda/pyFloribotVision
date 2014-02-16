#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from ConfigParser import ConfigParser


class ConfigController(object):
    def __init__(self, configFileName):
        self.configFileName = configFileName
        self.rawConfig = self._loadFile()
        self.dictConfig = self.convertRawConfigToDict()

    def _loadFile(self):
        config = ConfigParser(allow_no_value=True)
        config.optionxform = str  # Preserve case in ConfigParser
        config.read(self.configFileName)
        return config

    def convertRawConfigToDict(self, rawConfig=None):
        if not rawConfig:
            rawConfig = self.rawConfig

        configDict = dict()
        sectionList = rawConfig.sections()

        for section in sectionList:
            sectionDict = dict()
            optionList = rawConfig.options(section)
            for option in optionList:
                sectionDict[option] = rawConfig.get(section, option, True)
            configDict[section] = sectionDict

        return configDict

    def getConfig(self):
        return self.dictConfig

    def getSection(self, sectionname):
        return self.dictConfig[sectionname] if sectionname in self.dictConfig else None

    def getOption(self, sectionname, optionname):
        # ToDo: Thinkover if its usefull...
        section = self.getSection(sectionname)
        assert isinstance(section, dict)
        return section[optionname] if section and optionname in section else None

    def _saveFile(self):
        with open(self.configFileName, 'w') as f:
            self.rawConfig.write(f)

