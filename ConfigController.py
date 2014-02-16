#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from ConfigParser import ConfigParser

class ConfigController(object):

    def __init__(self, configFileName):
        self.configFileName = configFileName
        self.rawConfig = self.loadFile()

    def loadFile(self):
        config = ConfigParser(allow_no_value=True)
        config.read(self.configFileName)

        #if len(config.sections()) == 0:
        #    config = self.loadDefault()

        return config



    """
    def loadDefault(self):
        config = ConfigParser(allow_no_value=True)

        tmpsection = 'GENERAL'
        config.add_section(tmpsection)
        config.set(tmpsection, 'modules', 'directCVSource, cvGaussBlur, screenCVImageOutput')
        config.set(tmpsection, '#runCycle', 'oneShoot, loop')
        config.set(tmpsection, 'runCycle', 'oneShoot')
        config.set(tmpsection, 'exitKey', 'q')


        tmpsection = 'directCVSource'
        config.add_section(tmpsection)
        config.set(tmpsection, 'basemodule', 'DirectCVCamSource')
        config.set(tmpsection, 'camId', '0')
        config.set(tmpsection, 'outputImageName', 'image')


        tmpsection = 'screenCVImageOutput'
        config.add_section(tmpsection)
        config.set(tmpsection, 'basemodule', 'ScreenCVImageOutput')
        config.set(tmpsection, 'inputImageName', 'image')

        tmpsection = 'cvGaussBlur'
        config.add_section(tmpsection)
        config.set(tmpsection, 'basemodule', 'CVGaussBlur')
        config.set(tmpsection, 'inputImageName', 'image')
        config.set(tmpsection, 'outputImageName', 'image')



        return config
    """


    def saveFile(self):
        with open(self.configFileName, 'w') as f:
            self.rawConfig.write(f)



if __name__ == "__main__":
    cc = ConfigController('default.conf')
    #cc.saveFile()