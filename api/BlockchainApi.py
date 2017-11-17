#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import time

from api.BaseApi import BaseApi

# https://api.blockchain.info/stats
class BlockchainApi(BaseApi):
    baseDomain = "https://api.blockchain.info"

    def getStatsPath(self):
        return self.baseDomain + "/stats"

    def sanitizeStatsData(self, data):
        now_date_format = '%Y-%m-%dT%H:%M:%S %z'

        data['date'] = datetime.datetime.fromtimestamp(
            data['timestamp'] / 1e3
        )

        data['created_at'] = time.strftime(now_date_format, time.localtime())
        data['created_at'] = datetime.datetime.strptime(data['created_at'], now_date_format)

        return data

    def getStats(self):
        try:
            response = self.requests.get(self.getStatsPath())
        except Exception as e:
            raise e

        return self.sanitizeStatsData(response.json())

