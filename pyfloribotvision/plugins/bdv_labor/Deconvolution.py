#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.




from pyfloribotvision.types.NameType import NameType
from pyfloribotvision.types.FloatType import FloatType
from pyfloribotvision.types.IntType import IntType

from .. BasePlugin import BasePlugin
import cv2
import numpy as np

class Deconvolution(BasePlugin):

    configParameter = [
        NameType('inputImageName', input=True),
        NameType('outputImageName', output=True)
    ]

    def __init__(self, **kwargs):
        super(Deconvolution, self).__init__(**kwargs)


    def preCyclicCall(self):
        hlut = np.sin(np.linspace(0, np.pi, 31))
        hblk = np.zeros(180-hlut.size, np.float32)
        hlut = np.concatenate((hlut, hblk))
        self.hlut = np.roll(hlut, 24)

        flut = np.sin(np.linspace(0, np.pi*0.5, 256))*255
        fblk = np.zeros(256-flut.size, np.float32)
        self.flut = np.concatenate((flut, fblk))

        tflut = np.sin(np.linspace(0, np.pi*0.8, 256))*255
        tfblk = np.zeros(256-tflut.size, np.float32)
        self.tflut = np.concatenate((tflut, tfblk))


    def externalCall(self):
        image = self.inputImageName.data


        imagef = np.float32(image)/255.0
        d = 60
        noise = 10**(-0.1*5)
        psf = self.defocus_kernel(d, 100)
        cv2.imshow('psf', psf)


        #cv2.imshow('spektralblur',spektralblur)

        bluredge = self.blur_edge(imagef)
        se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
        bluredge = cv2.erode(bluredge, se)



        dftimg = cv2.dft(bluredge, flags=cv2.DFT_COMPLEX_OUTPUT)

        #----

        psf /= psf.sum()
        psf_pad = np.zeros_like(bluredge)
        kh, kw = psf.shape
        psf_pad[:kh, :kw] = psf
        PSF = cv2.dft(psf_pad, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows=kh)
        PSF2 = (PSF**2).sum(-1)
        iPSF = PSF / (PSF2 + noise)[..., np.newaxis]
        RES = cv2.mulSpectrums(dftimg, iPSF, 0)
        deconvolve = cv2.idft(RES, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT )
        deconvolve = np.roll(deconvolve, -kh//2, 0)
        deconvolve = np.roll(deconvolve, -kw//2, 1)

        self.outputImageName.data = deconvolve


    def defocus_kernel(self, d, sz=65):
        kern = np.zeros((sz, sz), np.uint8)
        cv2.circle(kern, (sz, sz), d, 255, -1, cv2.CV_AA, shift=1)
        kern = np.float32(kern) / 255.0
        return kern


    def blur_edge(self, img, d=31):
        h, w  = img.shape[:2]
        img_pad = cv2.copyMakeBorder(img, d, d, d, d, cv2.BORDER_WRAP)
        img_blur = cv2.GaussianBlur(img_pad, (2*d+1, 2*d+1), -1)[d:-d,d:-d]
        y, x = np.indices((h, w))
        dist = np.dstack([x, w-x-1, y, h-y-1]).min(-1)
        w = np.minimum(np.float32(dist)/d, 1.0)
        return img*w + img_blur*(1-w)
