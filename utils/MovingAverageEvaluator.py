from datetime import datetime, timedelta
import pymongo

class MovingAverageEvaluator:

    def __init__(self, dbManager):
        self.dbManager = dbManager


    def run(self, avg_minutes,avg_field):
        docBuffer = []
        writeBuffer = []

        for doc in self.dbManager.db["test_query_collection"].find({avg_field: {"$exists": False}}).sort('date',pymongo.ASCENDING):
        # for doc in self.dbManager.fundCollection.find().sort('date',pymongo.ASCENDING):
          docBuffer.append(doc)        # Add to buffer
          print(doc)
          exit()

          # Filter buffer for expired
          docBuffer = filter(lambda x: x['date'] >= (doc['date'] - timedelta(minutes=avg_minutes)), docBuffer)

          writeBuffer.append({
            "updateOne": {
              "filter": { "_id": doc['_id'] },
              "update": {
                "$set": {
                  avg_field: reduce(lambda x,y: y['bid'] + x, docBuffer, 0) / len(docBuffer),
                }
              }
            }
          })

          # Write if buffer has enough to make a bulk write
          if len(writeBuffer) > 10:
            collection.bulk_write(writeBuffer);
            writeBuffer = []

        # Clear any buffered writes
        if len(writeBuffer) > 0:
          collection.bulk_write(writeBuffer);
          writeBuffer = []