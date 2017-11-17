#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from api.BaseApi import BaseApi

class BitfinexApi(BaseApi):
    MAX_ORDERBOOK_LENGTH = 20
    baseDomain = "https://api.bitfinex.com/v1"

    def getTickerPath(self, coinfrom, cointo):
        symbol = coinfrom.lower() +cointo.lower()
        return self.baseDomain + "/pubticker/%s" % symbol

    def getOrderBookPath(self, coinfrom, cointo, limit):
        if not limit:
            limit = self.MAX_ORDERBOOK_LENGTH

        symbol = coinfrom.upper() +cointo.upper()

        return self.baseDomain + "/book/%s?limit_bids=%s&limit_asks=%s" % (symbol, limit, limit)

    def sanitizeOrderBookData(self, data):
        return data

    def getTicker(self, coinfrom, cointo):
        try:
            response = self.requests.get(self.getTickerPath(coinfrom, cointo))
        except Exception as e:
            raise e

        return response.json()

    def getOrderBook(self, coinfrom, cointo, limit=False):
        try:
            response = self.requests.get(self.getOrderBookPath(coinfrom, cointo, limit))
        except Exception as e:
            raise e

        return self.sanitizeOrderBookData(response.json())