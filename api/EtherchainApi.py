#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from api.BaseApi import BaseApi

class EtherchainApi(BaseApi):
    baseDomain = "https://etherchain.org/api"

    def getBlockCountPath(self):
        return self.baseDomain + "/blocks/count"

    def getTxForBlockPath(self, blockIdOrHash):
        return self.baseDomain + "/block/%s/tx" % blockIdOrHash

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