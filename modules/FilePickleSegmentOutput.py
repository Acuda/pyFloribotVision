#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from BaseModule import BaseModule
import cv2
import os
import logging
import pickle
import numpy as np


class FilePickleSegmentOutput(BaseModule):
    obligatoryConfigOptions = {'inputImageName': None, 'inputContourName': None, 'inputContourIndexListName': None,
                               'outputFile': None, 'overwriteExistingFile': None, 'createFilePath': None,
                               'cacheCycles': None}


    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')


    def postOptActions(self):
        self.pickleCycleCntr = 0;
        self.pickleCache = list()


    def externalCall(self):
        self.cacheCycles = int(self.cacheCycles)

        self.appendOutputDataToCache()

        if self.cacheCycles is not -1 and self.pickleCycleCntr >= self.cacheCycles:
            self.writeCacheToFile()
        self.pickleCycleCntr += 1


    def preOptActions(self):
        self.writeCacheToFile()

    def appendOutputDataToCache(self):
        image = self.ioContainer[self.inputImageName]
        cont = self.ioContainer[self.inputContourName]
        if self.inputContourIndexListName in self.ioContainer:
            contidx = self.ioContainer[self.inputContourIndexListName]
        else:
            contidx = range(len(cont))

        self.ioContainer[self.inputImageName]

        #create

        shape = list(image.shape[0:2])
        #shape = list(image.shape)
        shape.insert(0, len(contidx))
        shape = tuple(shape)

        ccimage = np.zeros(shape, np.uint8)


        for k, v in enumerate(contidx):
            cv2.drawContours(ccimage[k], cont, v, (255, 255, 255), -1)

        if len(ccimage) != 0:


            singleImageDump = list()



            #each found segment in image
            for segmentid, segmentcnt in enumerate(ccimage):


                shapePointList = list()
                for shapepoint in cont[contidx[segmentid]]:
                    x = shapepoint[0][0]
                    y = shapepoint[0][1]
                    shapePointList.append([x, y])

                #print len(shapePointList)

                #slows down at all... cpu vrom <40% up tu 100%!
                #needs a better way to do it
                # stackoverflow meaning: do it with pure python instead iterating an numpy obj

                segmentObjPoints = list()
                pixlist = np.nonzero(segmentcnt)
                for xk, y in enumerate(pixlist[0]):
                    x = pixlist[1][xk]
                    segmentObjPoints.append([x, y, image[y][x][2], image[y][x][1], image[y][x][0]])


                #also slow.... (slower than before...)
                """
                #python way...?
                print segmentcnt.shape
                pixlist = list()
                segmentObjPoints = list()
                for y, ycnt in enumerate(segmentcnt):

                    for x, value in enumerate(ycnt):
                        if value != 0:
                            #yraw = image[y]
                            #xraw = yraw[x]
                            #pixlist.append([x, y, xraw[2], xraw[1], xraw[0]])

                            pixlist.append([x, y, image[y][x][2], image[y][x][1], image[y][x][0]])
                """



                singleImageDump.append({'shapePointList': shapePointList, 'segmentObjPoints': segmentObjPoints})

            if len(singleImageDump) > 0:
                self.pickleCache.append(singleImageDump)
        """"""

    def writeCacheToFile(self):
        #print 'chache length', len(self.pickleCache)
        self.pickleCache = list()

        #directory = os.path.dirname(self.outputFile)

        #if not os.path.exists(directory):
        #    os.makedirs(directory)

        #pickle.dump(contidx, open(self.outputFile, 'wb'))

