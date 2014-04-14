#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.

from pyVisionGui import pyVisionGui

class GuiThreadX():


    def guithread(self):
        from threading import Thread
        '''run in thread'''
        thread = Thread(target=self.gui)#, args=('if any'))
        thread.start()

    def guiprocess(self):
        from multiprocessing import Process
        '''run in process'''
        process = Process(target=self.gui)#, args=('if any'))
        process.start()

    def gui(self):
        pvg = pyVisionGui()
        pvg.runGui()
