#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.


from BaseType import BaseType

class BaseListType(BaseType):
    def __init__(self, name=None, **kwargs):
        self.type = list
        super(BaseListType, self).__init__(name, **kwargs)
        self.itemtype = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self._splitList(value, ',', self.itemtype)


    def _splitList(self, value, delimiter, subtype=None):
        if type(value) is not self.type:
            value = [x.strip() for x in value.split(delimiter) if len(x)]
        if subtype:
            value = [subtype(x) for x in value]
        return value

    def __getitem__(self, item):
        return self.value[item]

    def __iter__(self):
        return iter(self.value)

    def invokeCallbacks(self, data):
        if isinstance(data, dict):
            for k, v in self._data.items():
                for cb in self._DataCallbackList:
                    cb(k, v)
        else:
            super(BaseListType, self).invokeCallbacks(data)


    def dataUpdateCallback(self, name, data):
        if name in self.value:
            if self.data is None:
                self._data = dict()
            self.data[name] = data

    def setDataValue(self, key, value):
            if self.data is None:
                self._data = dict()
            self.data[key] = value
            self.invokeCallbacks(self._data)

