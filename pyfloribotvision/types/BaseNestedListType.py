#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED. IN NO  EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM
# THE USE OF THIS SOURCE-CODE. USE AT YOUR OWN RISK.



from BaseListType import BaseListType

class BaseNestedListType(BaseListType):
    def __init__(self, name=None, **kwargs):
        super(BaseNestedListType, self).__init__(name, **kwargs)
        self.itemtype = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        value = self._splitList(value, ';')
        self._value = [self._splitList(x, ',', self.itemtype) for x in value]


