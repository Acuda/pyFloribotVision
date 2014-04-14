#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#Author: Björn Eistel
#Contact: <eistel@gmail.com>
#
# THIS SOURCE-CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO 
# EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOURCE-CODE. 
# USE AT YOUR OWN RISK.


from BaseType import BaseType

class BoolType(BaseType):
    def __init__(self, name=None, **kwargs):
        super(BoolType, self).__init__(name, **kwargs)
        self.type = self._convertToBool

    def _convertToBool(self, value):
        return str(value) == str(True)