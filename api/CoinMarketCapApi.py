#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import datetime

from api.BaseApi import BaseApi


class CoinMarketCapApi(BaseApi):
    baseDomain= "https://api.coinmarketcap.com/v1"

    def getTickerPath(self,start,limit):
        return self.baseDomain + "/ticker/?start=%s&limit=%s&convert=EUR" % (start, limit)

    def sanitizeTickerData(self, data):


        now_date_format = '%Y-%m-%dT%H:%M:%S %z'
        for element in data:

            element['created_at'] = time.strftime(now_date_format, time.localtime())
            element['created_at'] = datetime.datetime.strptime(element['created_at'], now_date_format)


            element['last_updated_datetime'] = datetime.datetime.fromtimestamp(
                int(element['last_updated'])
            )

        return data

    def getTicker(self, start=0, limit=30):
        try:
            response = self.requests.get(self.getTickerPath(start, limit))
        except Exception as e:
            raise e

        return self.sanitizeTickerData(response.json())

