#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.


from pyfloribotvision.types.StringType import StringType
from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.BoolType import BoolType
from pyfloribotvision.types.IntType import IntType
from .. BasePlugin import BasePlugin
import cv2
import logging
import pickle
import numpy as np
import time


class FilePickleSegmentOutput(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('inputContourName', input=True),
        NameType('inputContourIndexListName', input=True),
        StringType('outputFile'),
        BoolType('overwriteExistingFile'),
        BoolType('createFilePath'),
        IntType('cacheCycles'),
        BoolType('skipDump'),
    ]

    def __init__(self, **kwargs):
        super(FilePickleSegmentOutput, self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')
        self.timelist = list()

    def preCyclicCall(self):
        self.log.debug('preCyclicCall called')
        self.pickleCycleCntr = 0
        self.pickleCache = list()
        self.log.debug('open dataFile at <%s> in mode "write binary"', self.outputFile.value)
        self.dataFile = open(self.outputFile.value, 'wb')

    def externalCall(self):

        self.log.debug('externalCall called')
        self.appendOutputDataToCache()

        if self.cacheCycles.value is not -1 and self.pickleCycleCntr >= self.cacheCycles.value:
            self.writeCacheToFile()
            self.pickleCycleCntr = -1
        self.pickleCycleCntr += 1

        if len(self.timelist) > 0:
            print sum(self.timelist) / float(len(self.timelist))

    def postCyclicCall(self):
        self.log.debug('postCyclicCall called')
        self.writeCacheToFile()
        self.dataFile.close()

    def appendOutputDataToCache(self):
        image = self.inputImageName.data
        cont = self.inputContourName.data

        if len(self.inputContourIndexListName.data) > 0:
            contidx = self.inputContourIndexListName.data
        else:
            contidx = range(len(cont))

        #create

        #ToDo: Now there is a new Plugin called 'CreateContourBinaryImage'. Use it!

        shape = list(image.shape[0:2])
        #shape = list(image.shape)
        shape.insert(0, len(contidx))
        shape = tuple(shape)

        ccimage = np.zeros(shape, np.uint8)

        for k, v in enumerate(contidx):
            cv2.drawContours(ccimage[k], cont, v, (255, 255, 255), -1)

        singleImageDump = list()
        #each found segment in image
        for segmentid, segmentcnt in enumerate(ccimage):

            pixlist = np.nonzero(segmentcnt)
            singleImageDump.append([cont[contidx[segmentid]], pixlist])

        #if len(singleImageDump) > 0:
        self.pickleCache.append(image)
        self.pickleCache.append(singleImageDump)


    def writeCacheToFile(self):
        self.log.debug('check if skipDump <%s>', self.skipDump.value)
        if self.skipDump.value:
            self.log.debug('writeCacheToFile method is skipped')
            return

        #ToDo: create directory if not exist and allowed

        cnt = 2
        cntmax = len(self.pickleCache)
        objectDumpNames = ['raw-image', 'segments']
        self.log.debug('dump %d frames to file <%s>', cntmax, self.outputFile.value)
        for data in self.pickleCache:
            stime = time.time()
            self.log.debug('Frame %d of %d (%s)', cnt / 2, cntmax / 2, objectDumpNames[cnt % 2])
            pickle.dump(data, self.dataFile, -1)
            self.log.debug('Time to save file: %f3', (time.time() - stime)*1000)
            cnt += 1
        print
        self.pickleCache = list()



