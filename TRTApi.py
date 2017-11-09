#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import datetime
import time

# http://docs.python-requests.org/en/v0.5.0/api/
class TRTApi:
    MAX_ORDERBOOK_LENGTH = 20
    baseDomain = "https://api.therocktrading.com/v1"
    def __init__(self,api_key=False, api_secret=False):
        self.api_key=api_key
        self.api_secret=api_secret

    def getTickerPath(self, fund="BTCEUR"):
        return self.baseDomain + "/funds/%s/ticker" % fund

    def getOrderBookPath(self, fund="BTCEUR"):
        return self.baseDomain + "/funds/%s/orderbook" % fund


    def sanitizeTickerData(self, data):
        dateFormat = '%Y-%m-%dT%H:%M:%S.%f%z'
        last_colon_position = data['date'].rfind(":")
        data['date'] = data['date'][:last_colon_position] + data['date'][last_colon_position+1:]
        data['date'] = datetime.datetime.strptime(data['date'], dateFormat)

        now_date_format = '%Y-%m-%dT%H:%M:%S %z'
        data['created_at'] = time.strftime(now_date_format, time.localtime())
        data['created_at'] = datetime.datetime.strptime(data['created_at'], now_date_format)
        return data

    def sanitizeOrderBookData(self, data):
        dateFormat = '%Y-%m-%dT%H:%M:%S.%f%z'
        last_colon_position = data['date'].rfind(":")
        data['date'] = data['date'][:last_colon_position] + data['date'][last_colon_position+1:]
        data['date'] = datetime.datetime.strptime(data['date'], dateFormat)

        data['asks'] = data['asks'][:self.MAX_ORDERBOOK_LENGTH]
        data['bids'] = data['bids'][:self.MAX_ORDERBOOK_LENGTH]
        return data

    def getTicker(self, fund="BTCEUR"):
        try:
            response = requests.get(self.getTickerPath(fund))
        except Exception as e:
            raise e

        return self.sanitizeTickerData(response.json())

    def getOrderBook(self, fund="BTCEUR"):
        try:
            response = requests.get(self.getOrderBookPath(fund))
        except Exception as e:
            raise e

        return self.sanitizeOrderBookData(response.json())