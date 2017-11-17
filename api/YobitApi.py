#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from api.BaseApi import BaseApi

class YobitApi(BaseApi):
    MAX_ORDERBOOK_LENGTH = 20
    baseDomain = "https://yobit.net/api/3"

    def getOrderBookPath(self, coinfrom, cointo, limit=False):
        if not limit:
            limit = self.MAX_ORDERBOOK_LENGTH

        coinfrom = coinfrom.lower()
        cointo = cointo.lower()

        return self.baseDomain + "/depth/%s_%s?limit=%s" % (coinfrom, cointo, limit)

    def sanitizeOrderBook(self, data, coinfrom, cointo):

        data_key = "%s_%s" % (coinfrom.lower(), cointo.lower())

        result = {"asks":[], "bids":[]}
        for a in data[data_key]["asks"]:
            result["asks"].append({"price":a[0],"amount":a[1]})

        for b in data[data_key]["bids"]:
            result["bids"].append({"price":b[0],"amount":b[1]})
        return result

    def getOrderBook(self, coinfrom, cointo, limit=False):

        try:
            response = self.requests.get(self.getOrderBookPath(coinfrom, cointo, limit))
        except Exception as e:
            raise e

        return self.sanitizeOrderBook(response.json(), coinfrom, cointo)

