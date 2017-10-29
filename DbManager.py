from pymongo import MongoClient

FUND_COLLECTION = "fund"
ORDERBOOK_COLLECTION = "orderbook"
WHALECALLS_COLLECTION = "whalecalls"

FUND_CACHE_SIZE = 5

class DbManager:
    fundCache = []
    def __init__(self, host, dbName, user=False, password=False ):
        self.host = host
        self.user = user
        self.password = password

        try:
            self.client = MongoClient('localhost', 27017)
            self.db = self.client[dbName]
        except Exception as e:
            raise e

        if user:
            try:
                self.db.authenticate(user, password)
            except Exception as e:
                raise e

        self.fundCollection = self.db[FUND_COLLECTION]
        self.orderbookCollection = self.db[ORDERBOOK_COLLECTION]
        self.whaleCallsCollection = self.db[WHALECALLS_COLLECTION]

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
        if len(self.fundCache) >= FUND_CACHE_SIZE:
            result = self.fundCollection.insert_many(self.fundCache)
            self.fundCache = []
        else:
            self.fundCache.append(data)

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


# ORDERBOOK
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





