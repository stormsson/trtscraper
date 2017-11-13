#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import datetime
import time

from api.BaseApi import BaseApi

# https://api.blockchain.info/stats
class BlockchainApi(BaseApi):
    baseDomain = "https://api.blockchain.info"

    def getStatsPath(self):
        return self.baseDomain + "/stats"

    def sanitizeStatsData(self, data):
        dateFormat = '%Y-%m-%dT%H:%M:%S.%f%z'

        data['date'] = datetime.datetime.fromtimestamp(
            data['timestamp'] / 1e3
        ).strftime(dateFormat)

        return data

    def getStats(self):
        try:
            response = self.requests.get(self.getStatsPath())
        except Exception as e:
            raise e

        return self.sanitizeStatsData(response.json())

