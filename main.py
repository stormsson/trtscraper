import time
import os

from Scraper import Scraper
from Config import Config
from DbManager import DbManager

configDir = os.path.dirname(os.path.realpath(__file__)) + "/config"

try:
    dbConfig = Config.readDB(configDir + "/db.yml")
except FileNotFoundError as e:
    dbConfig = False

if not dbConfig:
    print("No Database configuration found!")
    exit()

dbManager = DbManager(dbConfig['host'], dbConfig['dbName'])

scraper = Scraper()

"""
'open': 4059.15,
'fund_id': 'BTCEUR',
'ask': 4810.39,
'close': 4450.0,
'last': 4808.74,
'high': 4503.59,
'date': '2017-10-13T20:03:56.867+02:00',
'bid': 4807.36,
'volume': 1387610.08,
'low': 4035.12,
'volume_traded': 358.151
}
"""

lastDate = False
while True:
    data = scraper.getTicker()

    if lastDate != data['date']:
        lastDate = data['date']
        dbManager.saveFund(data)

    time.sleep(5)


