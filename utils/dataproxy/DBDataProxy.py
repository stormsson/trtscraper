#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import datetime

from utils.dataproxy.BaseDataProxy import BaseDataProxy

class DBDataProxy(BaseDataProxy):

    def __init__(self, dbManager):
        self.dbManager = dbManager
        self.starting_datetime = False

        self.init_time = datetime.datetime.now()

    def setStartingDateTime(self, starting_datetime):
        self.starting_datetime = starting_datetime

    def calculateCurrentTime(self):

        current_datetime = datetime.datetime.now()

        # delta = current time - self.init_time
        # current_elab_date = starting_datetime + delta


    def getLastTickerData(self, fund_id):
        return self.dbManager.fundCollection.find({
            "fund_id":fund_id,
            "created_at": {"$gte": self.starting_datetime }
            }).sort("created_at", 1).limit(1)[0]

    def getLastOrderbookData(self, fund_id):
        return self.dbManager.getLastOrderbook(fund_id)