#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient

FUND_COLLECTION = "fund"
ORDERBOOK_COLLECTION = "orderbook"
WHALECALLS_COLLECTION = "whalecalls"
STATS_COLLECTION = "stats"

FUND_CACHE_SIZE = 0

class DBManager:
    fundCache = []

    @staticmethod
    def createDBManager(host, dbName, user=False, password=False):
        try:
            client = MongoClient('localhost', 27017)
            db = client[dbName]
        except Exception as e:
            raise e

        if user:
            try:
                db.authenticate(user, password)
            except Exception as e:
                raise e

        return DBManager(db)

    def __init__(self,  db):

        self.db = db

        self.fundCollection = self.db[FUND_COLLECTION]
        self.orderbookCollection = self.db[ORDERBOOK_COLLECTION]
        self.whaleCallsCollection = self.db[WHALECALLS_COLLECTION]
        self.statsCollection = self.db[STATS_COLLECTION]

        # self.fundCollection.remove()
        # self.orderbookCollection.remove()
        # self.whaleCallsCollection.remove()
        # exit()


    def DELETEEVERYTHING():
        self.fundCollection.remove()
        self.orderbookCollection.remove()
        self.whaleCallsCollection.remove()
        exit()

# FUNDS
    def saveFund(self, data):
        if FUND_CACHE_SIZE:
            if len(self.fundCache) >= FUND_CACHE_SIZE:
                result = self.fundCollection.insert_many(self.fundCache)
                self.fundCache = []
            else:
                self.fundCache.append(data)
        else:
            result = self.fundCollection.insert_one(data)



        return
        # last_id = self.fundCollection.insert_one(data).inserted_id
        # return last_id


#{ date: {$gte: ISODate("2017-10-24T20:27:00.000+02:00")}}

    def findFundByDate(self, fund_id, date_from, date_to, include_date_to=False):
        inclusion_parameter = "$lt"
        if include_date_to:
            inclusion_parameter = "$lte"

        return self.fundCollection.find({ "date" : {
            "$gte": date_from,
            inclusion_parameter: date_to
        } })

    def getLastFund(self, fund_id):
        res = self.fundCollection.find({"fund_id":fund_id}).sort("created_at", -1).limit(1)[0]
        return res



# ORDERBOOK
    def getLastOrderBook(self, fund_id):
        res = self.orderbookCollection.find({"fund_id":fund_id}).sort("date", -1).limit(1)[0]
        return res

    def saveOrderBook(self, data):
        last_id = self.orderbookCollection.insert_one(data).inserted_id
        return last_id

# WHALECALLS
    def saveWhaleCalls(self, data):
        if isinstance(data, dict):
            last_id = self.whaleCallsCollection.insert_one(data).inserted_id
            return last_id

        if isinstance(data, list):
            result = self.whaleCallsCollection.insert_many(data)
            return result.inserted_ids

    def findWhaleCallsByIds(self, ids):
        return self.whaleCallsCollection.find({ "id_str" : {"$in": ids} })

# STATS
    def saveStats(self, data):
        if isinstance(data, dict):
            last_id = self.statsCollection.insert_one(data).inserted_id
            return last_id

        if isinstance(data, list):
            result = self.statsCollection.insert_many(data)
            return result.inserted_ids




