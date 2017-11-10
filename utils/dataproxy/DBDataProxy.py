#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from BaseDataProxy import BaseDataProxy
from DBManager import DBManager

class DBDataProxy(BaseDataProxy):

    def __init__(self, dbManager):
        self.dbManager = dbManager

    def getLastTickerData(self, fund_id):
        return self.dbManager.getLastFund(fund_id)


    def getLastOrderbookData(self, fund_id):
        return self.dbManager.getLastOrderbook(fund_id)