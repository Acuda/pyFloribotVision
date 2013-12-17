#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT WILL 
# THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.

import pickle
import cv2
import numpy as np
import random


def viewPoints(singleImageDump):
    #find max coord...
    maxpoints = list()
    for k, segment in enumerate(singleImageDump):
        maxpoints.append([0, 0])
        for point in segment[0]:  # segment[0] -> shapePointList
            #print point
            #print point[0][0],
            if point[0] > maxpoints[k][0]:
                maxpoints[k][0] = point[0]
            if point[1] > maxpoints[k][1]:
                maxpoints[k][1] = point[1]

    #just showing its the same...
    maxvalues = list()
    for k, segment in enumerate(singleImageDump):
        maxvalues.append([0, 0])
        for value in segment[1]:  # segment[1] -> segmentObjPoints
            if value[0] > maxvalues[k][0]:
                maxvalues[k][0] = value[0]
            if value[1] > maxvalues[k][1]:
                maxvalues[k][1] = value[1]

    print 'max point coords', maxpoints
    print 'max value coords', maxvalues

    #overall max incl. offset
    xmax = max([x[0] for x in maxpoints]) + 20 if len(maxpoints) else 20
    ymax = max([x[1] for x in maxpoints]) + 20 if len(maxpoints) else 20

    #build image...
    sample = np.zeros((ymax, xmax, 3), np.uint8)
    sample += 127  # adding 50% grey for better control that shows RGB(0,0,0) is not RGB(0,0,1)
    for k, segment in enumerate(singleImageDump):
        maxvalues.append([0, 0])
        for value in segment[1]:  # segment[1] -> segmentObjPoints
            sample[value[1]][value[0]] = value[4], value[3], value[2]



    rnd = random.Random()
    sampleCont = sample.copy()
    for k, segment in enumerate(singleImageDump):
        color = [120, 120, 120]
        color[rnd.randint(0, 2)] = rnd.randint(20, 25) * 10
        color = tuple(color)

        segm = np.array(segment[0])  # segment[0] -> shapePointList
        cv2.drawContours(sampleCont, [segm], -1, color)

    #show image
    return sample, sampleCont


if __name__ == "__main__":
    f = open("/tmp/pyFloribotVideoSegments.pickle", "rb")
    #f = open("../data/videoSegments_new.pickle", "rb")

    framelist = list()


    print 'preload & calculate data'
    cnt = 1
    try:
        while True:
            print
            print 'recover frame:', cnt
            cnt += 1
            image = pickle.load(f)
            singleImageDump = pickle.load(f)
            sample, samplecont = viewPoints(singleImageDump)

            framelist.append({
                              'original image': image,
                              'sample': sample,
                              'sample w. cont': samplecont,
                              })
    except:
        pass

    print

    dorun = True
    while dorun:
        for frame in framelist:
            for k, v in frame.items():
                cv2.imshow(k, v)

            if (cv2.waitKey(100) & 255) == ord('q'):
                dorun = False
                break



    f.close()