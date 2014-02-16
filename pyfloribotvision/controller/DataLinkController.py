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
    def __init__(self):
        self._data = dict()

    def getValue(self, item):
        return self[item]

    def __getitem__(self, item):
        return self._data[item]

    def setValue(self, key, value):
        self[key] = value

    def __setitem__(self, key, value):
        self._data[key] = value
