#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

from api.CoinMarketCapApi import CoinMarketCapApi
from entities.Stats import Stats

class CoinMarketCapScraper(object):
    def __init__(self, dbManager):
        self.dbManager = dbManager
        self.api = CoinMarketCapApi()

    def getTicker(self):
        data = False

        try:
            data = self.api.getTicker()
        except Exception as e:
            raise e

        data["TYPE"] = Stats.ID_BLOCKCHAINSTATS
        data["SYMBOL"] = "BTC"

        return data

    def run(self, waiting_seconds):
        last_timestamps = {}
        while True:
            data = self.getTicker()

            if(data):
                writing_buffer = []
                for el in data:

                    if(last_timestamp != stats["timestamp"]):
                        self.dbManager.saveStats(stats)
                        last_timestamp = stats["timestamp"]

            time.sleep(waiting_seconds)