#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from api.BaseApi import BaseApi


class CoinMarketCapApi(BaseApi):
    baseDomain= "https://api.coinmarketcap.com/v1"

    def getTickerPath(self,start,limit):
        return self.baseDomain + "/ticker/?start=%s&limit=%s" % (start, limit)

    def getTicker(self, start=0, limit=30):
        try:
            response = self.requests.get(self.getTickerPath(start, limit))
        except Exception as e:
            raise e

        return response.json()

