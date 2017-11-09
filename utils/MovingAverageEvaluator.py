from datetime import datetime, timedelta
from functools import reduce
import pymongo

from pymongo import UpdateOne


class MovingAverageEvaluator:

    def __init__(self, dbManager):
        self.dbManager = dbManager

    def evalAverageFromDate(self, start, window_minutes=15, avg_field="bid"):
        collection = self.dbManager.db["fund"]

        starting_datetime = start - timedelta(minutes=window_minutes)
        print("searching from: %s" % starting_datetime)

        field_value = 0
        cnt = 0
        for doc in collection.find({"created_at":{"$lte": starting_datetime}}).sort('created_at',pymongo.DESCENDING).limit(1):
            print(doc)
            field_value = field_value + doc[avg_field]
            if not field_value:
                field_value = doc[avg_field]
            cnt+=1

        if not cnt:
            cnt = 1


        print("field_value: %s , cnt: %s" % (field_value, cnt))

        return field_value/cnt


    def run(self, avg_minutes,avg_field, field_to_save):
        docBuffer = []
        writeBuffer = []

        collection = self.dbManager.db["fund"]

        # for doc in collection.find({date:{"$gt":"2017-10-31 00:00:00"}, field_to_save: {"$exists": False}}).sort('date',pymongo.ASCENDING):
        for doc in collection.find({"date":{"$gt": datetime(2017,10,31)}}).sort('date',pymongo.ASCENDING):
        # for doc in self.dbManager.fundCollection.find().sort('date',pymongo.ASCENDING):
            docBuffer.append(doc)        # Add to buffer


            # Filter buffer for expired
            filteredDocBuffer = filter(lambda x: x['date'] >= (doc['date'] - timedelta(minutes=avg_minutes)), docBuffer)

            filteredDocBuffer = list(filteredDocBuffer)

            bufferLength = len(filteredDocBuffer) if len(filteredDocBuffer) else 1

            field_value = reduce(lambda x,y: x + y[avg_field], filteredDocBuffer, 0) / bufferLength
            if not field_value:
                field_value = doc[avg_field]


            writeBuffer.append(UpdateOne(
                { "_id": doc['_id'] },
                { "$set": {
                        field_to_save: field_value
                        }
                }
            ))

            # Write if buffer has enough to make a bulk write
            if len(writeBuffer) > 300:
                collection.bulk_write(writeBuffer);
                writeBuffer = []

            # Clear any buffered writes
            if len(writeBuffer) > 0:
                collection.bulk_write(writeBuffer);
                writeBuffer = []



#db.test_query_collection.updateMany({"avg_5min":{$exists: true}},{$unset: {"avg_5min":""}})