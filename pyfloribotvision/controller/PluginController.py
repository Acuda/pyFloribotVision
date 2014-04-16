#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


import logging
from importlib import import_module


class PluginController(object):
    """The PluginController handles loading and finding of the Plugins"""


    def __init__(self, pluginprefix):
        """Initializes the PluginController and load its Plugins

        :param pluginprefix: 
        """

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self._plugindir = 'plugins'
        if pluginprefix != '':
            self._plugindir = pluginprefix + '.' + self._plugindir

        self._pluginList = None
        self._pluginListFlat = dict()

    def loadPluginClass(self, item):
        pkgd = '.'  # delimiter for packages

        pkgpath = self._plugindir + pkgd + item
        cname = item.split(pkgd)[-1:][0]

        self.log.debug('try import for <%s> in package <%s>', pkgpath, cname)

        try:
            imod = import_module(pkgpath)
        except ImportError as ex:
            self.log.critical('import for <%s>', pkgpath, exc_info=1)
            return None

        if hasattr(imod, cname):
            return getattr(imod, cname)
        else:
            self.log.error('loading of class <%s> in package <%s>', cname, pkgpath)

        return None
