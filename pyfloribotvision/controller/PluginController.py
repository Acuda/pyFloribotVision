#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from __future__ import print_function
import logging


class PluginController(object):
    """The PluginController handles loading and finding of the Plugins"""


    def __init__(self, pluginprefix):
        """Initializes the PluginController and load its Plugins"""

        self.log = logging.getLogger(__name__)
        self.log.debug('logging started')

        self._plugindir = 'plugins'
        if pluginprefix != '':
            self._plugindir = pluginprefix + '.' + self._plugindir

        self._pluginList = None
        self._pluginListFlat = dict()

    def loadPlugins(self, module=None, forceReload=False):
        """
        Load Plugins from 'plugin' package and returns them as dict

        Keyword arguments:
        module -- Python-Module to search in (default: None)
        forceReload -- True forces reload of cached PluginList (default: False)
        """

        self.log.debug('loadPlugins invoked for module: <%s>' % module)

        if self._pluginList is not None or not forceReload:
            self.log.debug('existing pluginList or reload forced, returning previously loaded list')
            return self._pluginList

        if module is None:
            try:
                self.log.debug('try import plugindir: <%s>' % self._plugindir)
                if '.' in self._plugindir:
                    plist = self._plugindir.split('.', 2)
                    module = __import__(plist[0])
                    for m in plist[1:]:
                        module = getattr(module, m)
                else:
                    module = __import__(self._plugindir)
            except ImportError as ex:
                self.log.error('fail to import PLUGINDIR %s',ex.message)
                return dict()

        self.log.debug(module.__name__ + str(dir(module)))

        pluginNameList = [x for x in dir(module) if not x.startswith('_')]
        pluginList = dict()

        for pluginName in pluginNameList:
            #first level, get submodule or class
            anonobj = getattr(module, pluginName)

            #python-way: instead of checking treat as class and handle error...
            try:
                objclass = getattr(anonobj, pluginName)
                pluginList[pluginName] = objclass
                self.log.debug('CLASS <%s> found in <%s>' % (objclass.__name__, module.__name__))
            except AttributeError:
                #not a class - assuming a submodule
                self.log.debug('MODULE <%s> found' % anonobj.__name__)
                pluginList[pluginName] = self.loadPlugins(anonobj)

        return pluginList

    def findPlugin(self, item, _itemList=None):
        """
        Find a Plugin and returns it if found, otherwise None

        item -- the Plugin to search for
            if item is an instance of str the format is according to a relative import
            in the plugin package. e.g.: 'opencv.cvDrawContours'
        _itemList -- only for recursion purpose, should not be used due to cache mechanisms
            (default: None)
        """

        if item in self._pluginListFlat.keys():
            return self._pluginListFlat[item]

        if _itemList is None:
            _itemList = self._pluginList
        if _itemList is None:
            self._pluginList = self.loadPlugins()
            _itemList = self._pluginList

        if isinstance(item, str):
            itemListKeys = _itemList.keys()

            if item in itemListKeys and not isinstance(_itemList[item], dict):
                self._pluginListFlat[_itemList[item].__module__.split('.', 1)[1]] = _itemList[item]
                return _itemList[item]

            if '.' in item:
                prefix, suffix = item.split('.', 1)
                if prefix in itemListKeys and isinstance(_itemList[prefix], dict):
                    return self.findPlugin(suffix, _itemList[prefix])

        return None

    def __contains__(self, item):
        """magic member for use with "in" keyword

        arguments:
        item  -- key object on the left side of in keyword"""
        return self.findPlugin(item) is not None
