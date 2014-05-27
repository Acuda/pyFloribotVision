#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


import logging
from importlib import import_module


class PluginController(object):
    """The PluginController handles the loading and finding of the Plugins"""


    def __init__(self, pluginprefix):
        """Initializes the PluginController and load its Plugins

        :param pluginprefix: the package-path where the plugin-package can be found
        :type pluginprefix: str
        """

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self._plugindir = 'plugins'
        if pluginprefix != '':
            self._plugindir = pluginprefix + '.' + self._plugindir

        self._pluginList = None
        self._pluginListFlat = dict()

    def loadPluginClass(self, item):
        """
        Loads a PluginClass by relativ path and returns it if found, otherwise None
        Due to conventions, the name of the PluginClass must be the same as the
        FileName containing the class.

        :param item: the Plugin to search for
            str of the format according to a relative import in the plugin package.
            e.g.: 'opencv.cvDrawContours'
        :type item: str

        :returns: the class of the loaded plugin or None if an error occurred
        """

        pkgd = '.'  # delimiter for packages
        print self._plugindir , pkgd , item
        pkgpath = self._plugindir + pkgd + item  # package-path
        cname = item.split(pkgd)[-1:][0]  # class-name

        self.log.debug('try import for <%s> in package <%s>', cname, pkgpath)

        try:
            imod = import_module(pkgpath)
        except ImportError:
            self.log.critical('import for <%s>', pkgpath, exc_info=1)
            return None

        if hasattr(imod, cname):
            return getattr(imod, cname)
        else:
            self.log.error('loading of class <%s> in package <%s>', cname, pkgpath)

        return None
