#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


class DataLinkController(object):
    """Class for data-exchange between the plugins"""
    def __init__(self):
        """Creates internal dictionary"""
        self._data = dict()

    def getValue(self, item):
        """Returns the value corresponding to key (item)

        :param item: key object in the square parenthesis
        :type item: object
        :returns: entry of the dictionary
        :rtype: object
        """
        return self[item]

    def __contains__(self, item):
        """magic member for use with "in" keyword

        :param item: key object on the left side of in keyword"""
        return item in self._data

    def __getitem__(self, item):
        """magic member for use with square parenthesis as getter

        :param item: key object in the square parenthesis
        :type item: object
        :returns: entry of the dictionary
        :rtype: object
        """
        return self._data[item]

    def setValue(self, key, value):
        """set value to the internal dictionary

        :param key: key to set
        :param value: value to set for the given key"""
        self[key] = value

    def __setitem__(self, key, value):
        """magic member for use with square parenthesis as getter

        :param key: key to set
        :param value: value to set for the given key
        """
        self._data[key] = value

    def keys(self):
        return self._data.keys()