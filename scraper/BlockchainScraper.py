#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

from api.BlockchainApi import BlockchainApi
from entities.Stats import Stats

class BlockchainScraper(object):

    def __init__(self, dbManager):
        self.dbManager = dbManager
        self.api = BlockchainApi()


    def getStats(self):
        data = False

        try:
            data = self.api.getStats()
        except Exception as e:
            raise e

        data["TYPE"] = Stats.ID_BLOCKCHAINSTATS
        data["SYMBOL"] = "BTC"

        return data

    def run(self, waiting_seconds):
        last_timestamp = False
        while True:
            stats = self.getStats()
            if(stats):
                if(last_timestamp != stats["timestamp"]):
                    self.dbManager.saveStats(stats)
                    last_timestamp = stats["timestamp"]

            time.sleep(waiting_seconds)
