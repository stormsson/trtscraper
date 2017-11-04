from datetime import datetime, timedelta
from functools import reduce
import pymongo

from pymongo import UpdateOne


class MovingAverageEvaluator:

    def __init__(self, dbManager):
        self.dbManager = dbManager


    def run(self, avg_minutes,avg_field, field_to_save):
        docBuffer = []
        writeBuffer = []

        collection = self.dbManager.db["test_query_collection"]

        for doc in collection.find({field_to_save: {"$exists": False}}).sort('date',pymongo.ASCENDING):
        # for doc in self.dbManager.fundCollection.find().sort('date',pymongo.ASCENDING):
            docBuffer.append(doc)        # Add to buffer


            # Filter buffer for expired
            docBuffer = filter(lambda x: x['date'] >= (doc['date'] - timedelta(minutes=avg_minutes)), docBuffer)
            for i in docBuffer:
                print(i)


            bufferLength = len(list(docBuffer)) if len(list(docBuffer)) else 1

            writeBuffer.append(UpdateOne(
                { "_id": doc['_id'] },
                { "$set": {
                        field_to_save: reduce(lambda x,y: y[avg_field] + x, docBuffer, 0) / bufferLength
                        }
                }
            ))

            # writeBuffer.append({
            #     "updateOne": {
            #         "filter": { "_id": doc['_id'] },
            #         "update": {
            #             "$set": {
            #                 field_to_save: reduce(lambda x,y: y[avg_field] + x, docBuffer, 0) / bufferLength,
            #             }
            #         }
            #     }
            # })

            # Write if buffer has enough to make a bulk write
            if len(writeBuffer) > 10:
                collection.bulk_write(writeBuffer);
                writeBuffer = []

            # Clear any buffered writes
            if len(writeBuffer) > 0:
                collection.bulk_write(writeBuffer);
                writeBuffer = []