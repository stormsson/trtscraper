#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dateutil.parser as dateParser

from api.BaseApi import BaseApi

class EtherchainApi(BaseApi):
    baseDomain = "https://etherchain.org/api"

    def getBlockCountPath(self):
        return self.baseDomain + "/blocks/count"

    def getTxForBlockPath(self, blockIdOrHash):
        return self.baseDomain + "/block/%s/tx" % blockIdOrHash

    def getTransactionsPath(self, offset=0, count=100):
        return self.baseDomain + "/txs/%s/%s" % (offset, count)


    def sanitizeBlockCountData(self, data):
        return int(data["data"]["count"])

    def getBlockCount(self):
        try:
            response = self.requests.get(self.getOrderBookPath(coinfrom, cointo, limit))
        except Exception as e:
            raise e

        return self.sanitizeBlockCountData(response.json())

    def sanitizeTxForBlockData(self, data):
        return data["data"]



    def getTxForBlock(self, blockIdOrHash):
        try:
            response = self.requests.get(self.getTxForBlockPath(blockIdOrHash))
        except Exception as e:
            raise e

        return self.sanitizeTxForBlockData(response.json())


    def sanitizeGetTxData(self, data):

        result = []
        for tx in data["data"]:
            tx['date'] = dateParser.parse(tx['time'])

            result.append(
                {
                    "hash": tx["hash"],
                    "price": int(tx["price"]),
                    "gasLimit": int(tx["gasLimit"]),
                    "gasUsed": int(tx["gasUsed"]),
                    "date": tx["date"],
                }
            )

        return result

    def getTransactions(self, offset=0, count=100):
        try:
            response = self.requests.get(self.getTransactionsPath(offset, count))
        except Exception as e:
            raise e


        return self.sanitizeGetTxData(response.json())
