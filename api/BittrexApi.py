#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from api.BaseApi import BaseApi

class BittrexApi(BaseApi):
    MAX_ORDERBOOK_LENGTH = 20
    baseDomain = "https://bittrex.com/api/v1.1"

    def getTickerPath(self, coinfrom, cointo):
        market = coinfrom.upper() +"-"+cointo.upper()
        return self.baseDomain + "/public/getticker?market=%s" % market

    def getOrderBookPath(self, coinfrom, cointo):
        market = coinfrom.upper() +"-"+cointo.upper()
        return self.baseDomain + "/public/getorderbook?market=%s&type=both" % market

    def sanitizeOrderBookData(self, data):
        result = {"asks":[], "bids":[]}
        for a in data["result"]["sell"]:
            result["asks"].append({"price":a["Rate"],"amount":a["Quantity"]})

        for b in data["result"]["buy"]:
            result["bids"].append({"price":b["Rate"],"amount":b["Quantity"]})

        result['asks'] = result['asks'][:self.MAX_ORDERBOOK_LENGTH]
        result['bids'] = result['bids'][:self.MAX_ORDERBOOK_LENGTH]
        return result

    def getTicker(self, coinfrom, cointo):
        try:
            response = self.requests.get(self.getTickerPath(coinfrom, cointo))
        except Exception as e:
            raise e

        return response.json()

    def getOrderBook(self, coinfrom, cointo):
        try:
            response = self.requests.get(self.getOrderBookPath(coinfrom, cointo))
        except Exception as e:
            raise e

        return self.sanitizeOrderBookData(response.json())