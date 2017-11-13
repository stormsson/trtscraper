#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseEntity(object):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

