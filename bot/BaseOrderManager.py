#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseOrderManager(object):

    def buy(self, amount, price):
        raise Exception("To be implemented")

    def sell(self, amount, price):
        raise Exception("To be implemented")