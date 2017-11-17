#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

from api.EtherchainApi import EtherchainApi

class EtherchainScraper(object):
    DEFAULT_SCRAPE_LIMIT=100

    def __init__(self, dbManager):
        self.dbManager = dbManager
        self.api = EtherchainApi()

    def run(self, waiting_seconds, scrape_limit=False):
        if not scrape_limit:
             scrape_limit = self.DEFAULT_SCRAPE_LIMIT


        while True:
            txs = self.api.getTransactions(0, scrape_limit)

            if(txs):
                self.dbManager.saveGasData(txs)

            time.sleep(waiting_seconds)
