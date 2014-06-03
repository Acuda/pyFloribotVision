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

class BaseType(object):

    def __init__(self, name, **kwargs):
        self.name =  name
        self._value = None
        if 'value' in kwargs:
            self.value = kwargs['value']

        self.constraint = None
        if 'constraint' in kwargs:
            self.constraint = kwargs['constraint']

        self.minValue = None
        if 'minValue' in kwargs:
            self.minValue = kwargs['minValue']

        self.maxValue = None
        if 'maxValue' in kwargs:
            self.maxValue = kwargs['maxValue']


        self.output = False
        if 'output' in kwargs:
            self.output = kwargs['output']

        self.input = False
        if 'input' in kwargs:
            self.input = kwargs['input']

        self.log = None

        self.type = None
        self._data = None

        self._logicSectionName = None

        self._DataCallbackList = list()

    def initLog(self):
        self.log = logging.getLogger(__name__)
        self._debugout('logging started for <%s>.<%s>', self._logicSectionName, self.name)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is not self.type:
            value = self.type(value)
        if self.checkConstraint(value):
            self._value = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        self.invokeCallbacks(data)

    def __add__(self, other):
        return self.__class__(value=self.value + self.type(other))

    def __sub__(self, other):
        return self.__class__(value=self.value - self.type(other))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.value == other.value
        else:
            return self.value == self.type(other)

    def checkConstraint(self, value):
        return value in self.constraint if self.constraint is not None else True

    def invokeCallbacks(self, data):
        for cb in self._DataCallbackList:
            self._debugout('invokeCallbacks for <%s> with value <%s>', cb,
                           self.value)
            cb(self.value, data)

    def registerDataUpdate(self, callback):
        self._debugout('registerDataUpdate for <%s>', callback)
        self._DataCallbackList.append(callback)

    def dataUpdateCallback(self, name, data):
        self._debugout('dataUpdateCallback for name <%s> and and section <%s>', name,
                       self._logicSectionName)

        #Todo: there should be a better way to do this... (quick fix)
        # skipping wrong data update...
        if name != self.value:
            return

        self.data = data

    def getConvertedValue(self, converter, *args):
        return self._convert(self.value, converter, *args)

    def getConvertedData(self, converter, *args):
        data = self.data
        if isinstance(data, dict):
            data = data.values()

        return self._convert(data, converter, *args)


    def _convert(self, data, converter, *args):
        return converter(data, *args)

    def _debugout(self, value, *args):
        self.log.debug('%s.%s: ' + value, self._logicSectionName, self.name, *args)
