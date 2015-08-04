#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


# HACK TO RUN OPENCV 2.x.x CODE UNDER OPENCV 3.x.x
import cv2
if cv2.__version__ >= '3.0.0':

    class OPENCV_DOWNWARD_COMPATIBILITY(object):
        CV_CAP_PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
        CV_CAP_PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

    import sys
    from cv2 import *  # DO NOT REMOVE THIS LINE!
    import opencv_version_hack
    sys.modules['cv2_original'] = cv2
    sys.modules['cv2'] = opencv_version_hack
    locals()['cv'] = OPENCV_DOWNWARD_COMPATIBILITY
