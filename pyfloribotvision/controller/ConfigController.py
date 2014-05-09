#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from ConfigParser import ConfigParser


class ConfigController(object):
    """Simple Wrapper for the ConfigParser. Loads the Configuration-File and Convert
    it's Data into
    a Dictionary Structure. Each Section becomes a Key for the tob-level dict and
    serves the Option Values in an concatenated-dict saved as section-value"""

    def __init__(self, configFileName):
        """Load the rawConfig from Config-File with the ConfigParser and convert the
        rawConfig into a dict structure

        :param configFileName: Path to the Configuration-File
        :type configFileName: str
        """
        self.configFileName = configFileName
        self.rawConfig = self._loadFile()
        self.dictConfig = self.convertRawConfigToDict()

    def _loadFile(self):
        """Loads the rawConfig with the ConfigParser, empty values are allowed and
        camel-case is preserved

        :returns: ConfigParser-Instance with loaded Config-File
        :rtype: ConfigParser
        """
        # allow comments (key-entry with leading #)
        config = ConfigParser(allow_no_value=True)
        # preserve camel-case in ConfigParser (readability)
        config.optionxform = str

        config.read(self.configFileName)
        return config

    def convertRawConfigToDict(self, rawConfig=None):
        """Converts the rawConfig into a dict structure and returns them

        :param rawConfig: rawConfig from ConfigParser, if ``None`` the previously
        loaded configuration will be converted (default None)

        :returns: converted configuration with sections on top level
        :rtype: dict
        """
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
        """simple getter for the converted configuration

        :returns: dictionary or None if no configuration was loaded
        :rtype: dict
        """
        return self.dictConfig


    def getSection(self, sectionname):
        """simple getter for a section (sub-dict) from the configuration (top-dict)

        :param sectionname: name of the section which will be returned
        :type sectionname: str

        :returns: sub-dictionary or None if no section found
        :rtype: dict
        """
        return self.dictConfig[sectionname] \
            if sectionname in self.dictConfig \
            else None

    def getOption(self, sectionname, optionname):
        """returns the value from the option which belongs to the given sectionname

        :param sectionname: name of the section
        :type sectionname: str
        :param optionname: name of the option which value will be returned
        :type optionname: str

        :rtype: str
        """

        # ToDo: Thinkover if its usefull...
        section = self.getSection(sectionname)
        assert isinstance(section, dict)
        return section[optionname] if section and optionname in section else None

        #
        #def _saveFile(self):
        #    with open(self.configFileName, 'w') as f:
        #        self.rawConfig.write(f)

