#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseDataProxy(object):

    def getLastTickerData(self, fund_id):
        raise Exception("To be implemented")

    def getLastOrderbookData(self, fund_id):
        raise Exception("To be implemented")