import pymongo
from pymongo import MongoClient

FUND_COLLECTION = "fund"
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


    def saveFund(self, data):
        last_id = self.fundCollection.insert_one(data).inserted_id
        return last_id





