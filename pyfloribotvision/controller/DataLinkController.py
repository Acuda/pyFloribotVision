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

        arguments:
        item -- key for internal dictionary
        """
        return self[item]

    def __contains__(self, item):
        """magic member for use with "in" keyword

        arguments:
        item  -- key object on the left side of in keyword"""
        return item in self._data

    def __getitem__(self, item):
        """magic member for use with square parenthesis as getter

        arguments:
        item -- key object in the square parenthesis"""
        return self._data[item]

    def setValue(self, key, value):
        """set value to the internal dictionary

        arguments:
        key -- key to set
        value -- value to set for the given key"""
        self[key] = value

    def __setitem__(self, key, value):
        """magic member for use with square parenthesis as getter

        arguments:
        key -- key to set
        value -- value to set for the given key"""
        self._data[key] = value
