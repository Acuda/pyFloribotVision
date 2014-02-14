#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE.
# USE AT YOUR OWN RISK.

import cv2
import pickle
import numpy as np
import os


def loadSingleFrame(filename):
    with open(filename, 'rb') as f:
        image = pickle.load(f)
        framedata = pickle.load(f)
    return image, framedata


def printout(indent, caption, value, clearfile=False):
    captionspace = 65
    valuespace = 10
    indentstr = '   '

    strtmp = (indentstr * (indent-1) + '{:%d} \t{:<%d}' %
           (captionspace - len(indentstr) * (indent-1), valuespace)).format(caption + ':', value)

    print strtmp

    filename = '/tmp/metadump.txt'
    if clearfile:
        try:
            os.remove(filename)
        except Exception as e:
            print e

    with open(filename, 'a') as f:
        f.write(strtmp + '\n')


def checkPixListDuplicateEntrys(pixlist):
    d = dict()
    for k, x in enumerate(pixlist[0]):
        y = pixlist.item(1, k)
        key = '%dx%d' % (x, y)
        if key in d:
            d[key] += 1
        else:
            d[key] = 0

    return sum(d.values()) > 0

def asciiDump(rawimage, framedata):
    wss = 5
    bds = 50
    capdeli = '-'*bds + '\n' + '-'*2 + ' '*wss + '%s' + '\n' + '-'*bds + '\n'
    #with open('../data/asciidump.txt', 'w') as f:
    with open('/tmp/asciidump.txt', 'w') as f:
        f.write(capdeli % 'Segments')

        for k, segment in enumerate(framedata):

            segmentcont = np.array(segment[0])
            segmentpointlist = np.array(segment[1])

            f.write('--  Seg. Cont. Nr. %d:\n' % k)
            segcontstrlist = [str(x[0]) for x in segmentcont]
            segcontstr = ', '.join(segcontstrlist).replace('  ', ' ')
            f.write(segcontstr)
            f.write('\n')


            f.write('--  Seg. Point-List. Nr. %d: \n' % k)
            pll = list()
            for k, x in enumerate(segmentpointlist[0]):
                y = segmentpointlist.item(1, k)
                key = '[%d %d]' % (x, y)
                pll.append(key)
            plstr = ', '.join(pll)
            f.write(plstr)
            f.write('\n')


        f.write(capdeli % 'RAW-Image-Frame')
        maxy = range(rawimage.shape[0])
        maxx = range(rawimage.shape[1])
        maxc = range(rawimage.shape[2])
        maxc.reverse()



        yl = list()
        for y in maxy:
            xl = list()
            for x in maxx:
                cl = list()
                for c in maxc:
                    cl.append(str(rawimage.item(y, x, c)))
                xl.append('[%s]' % ', '.join(cl))
            yl.append('[%s]' % ', '.join(xl))
            break
        f.write('[%s]' % ', '.join(yl))


if __name__ == "__main__":
    filename = '/tmp/pyFloribotVideoSegments.pickle'
    image, framedata = loadSingleFrame(filename)

    bytePerPixCord = 2
    bytePerColorPoint = 2

    print
    printout(1, 'Assume Size - Byte per Pixel-Coord', bytePerPixCord, True)
    printout(1, 'Assume Size - Byte per Color-Channel per Pixel', bytePerColorPoint)

    print
    printout(1, '#Segments in first Frame', len(framedata))

    for k, segment in enumerate(framedata):
        printout(2, 'Data of Segment Nr.', k)

        segmentcont = np.array(segment[0])
        segmentpointlist = np.array(segment[1])

        #-----

        print
        printout(3, 'Data of', 'RAW-Image-Frame')

        rawcalc = image.shape[0] * image.shape[1] * image.shape[2] * bytePerColorPoint
        printout(4, 'Calculated Size for Segment-Cont.-Data [Byte]', rawcalc)

        #-----

        print
        printout(3, 'Data of', 'Contour-List')

        contcalc = segmentcont.shape[0] * segmentcont.shape[1] * segmentcont.shape[2] * bytePerPixCord
        printout(4, 'Calculated Size for Segment-Cont.-Data [Byte]', contcalc)

        #-----

        print
        printout(3, 'Data of', 'Pixel-List')
        printout(4, 'Duplicate Entry in Pixel-List? [0 = False / 1 = True]', checkPixListDuplicateEntrys(segmentpointlist))

        pointcalc = segmentpointlist.shape[0] * segmentpointlist.shape[1] * bytePerPixCord
        printout(4, 'Calculated Size for Segment-Cont.-Data [Byte]', pointcalc)

        #------

        print
        totalsize = contcalc + pointcalc + rawcalc
        printout(2, 'Calculated total size of', 'Frame')
        printout(3, 'Framesize [MibByte]', totalsize / 1024.0 / 1024.0)


        #-----

        print
        printout(1, 'Comparison to:', 'RAW-File')
        fstat = os.stat(filename)
        printout(2, 'Real File-Size [MibByte]', fstat.st_size / 1024.0 / 1024.0)

        overheadsize = fstat.st_size - totalsize
        percent = overheadsize * 100.0 / fstat.st_size
        printout(2, 'Overhead [KibByte]', overheadsize / 1024.0)
        printout(2, 'Overhead [%]', percent)

    cv2.drawContours(image, [segmentcont], -1, (255, 255, 255))

    print


    asciiDump(image, framedata)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)