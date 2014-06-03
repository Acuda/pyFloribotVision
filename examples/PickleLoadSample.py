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
import time


def viewPoints(singleImageDump, image):

    shape = image.shape

    #build image...
    sample = np.zeros(shape, np.uint8)
    sample += 127  # adding 50% grey for better control that shows RGB(0,0,0) is not RGB(0,0,1)


    for segment in singleImageDump:

        print segment[1]
        for i in xrange(len(segment[1][0])):
            sample.itemset((segment[1][0][i], segment[1][1][i], 0), image.item(segment[1][0][i], segment[1][1][i], 0))
            sample.itemset((segment[1][0][i], segment[1][1][i], 1), image.item(segment[1][0][i], segment[1][1][i], 1))
            sample.itemset((segment[1][0][i], segment[1][1][i], 2), image.item(segment[1][0][i], segment[1][1][i], 2))

        cv2.imshow('sss', sample)

    rnd = random.Random()
    sampleCont = sample.copy()
    for k, segment in enumerate(singleImageDump):
        color = [120, 120, 120]
        color[rnd.randint(0, 2)] = rnd.randint(20, 25) * 10
        color = tuple(color)

        segm = np.array(segment[0])  # segment[0] -> shapePointList
        cv2.drawContours(sampleCont, [segm], -1, color)

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
            sample, samplecont = viewPoints(singleImageDump, image)

            framelist.append({
                              'original image': image,
                              'sample': sample,
                              'sample w. cont': samplecont,
                              })
    except:
        pass
    finally:
        pass

    print



    dorun = True
    while dorun:
        for frame in framelist:
            for k, v in frame.items():
                if k == 'sample':
                    cv2.imwrite('/tmp/sample.jpg', v)
                cv2.imshow(k, v)

            if (cv2.waitKey(150) & 255) == ord('q'):
                dorun = False
                break



    f.close()