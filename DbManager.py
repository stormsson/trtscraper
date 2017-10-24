from pymongo import MongoClient

FUND_COLLECTION = "fund"
ORDERBOOK_COLLECTION = "orderbook"
WHALECALLS_COLLECTION = "whalecalls"

class DbManager:
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


    def saveFund(self, data):
        last_id = self.fundCollection.insert_one(data).inserted_id
        return last_id

    def saveOrderBook(self, data):
        last_id = self.orderbookCollection.insert_one(data).inserted_id
        return last_id

    def saveWhaleCalls(self, data):
        if isinstance(data, dict):
            last_id = self.whaleCallsCollection.insert_one(data).inserted_id
            return last_id

        if isinstance(data, list):
            result = self.whaleCallsCollection.insert_many(data)
            return result.inserted_ids

    def findWhaleCallsByIds(self, ids):
        return self.whaleCallsCollection.find({ "id_str" : {"$in": ids} })





