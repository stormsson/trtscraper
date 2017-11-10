#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from TRTApi import TRTApi
from BaseDataProxy import BaseDataProxy

class TRTDataProxy(BaseDataProxy):

    def __init__(self, api):
        self.api= api

    def getLastTickerData(self, fund_id):
        return self.api.getTicker(fund_id)

    def getLastOrderbookData(self, fund_id):
        return self.api.getOrderBook(fund_id)