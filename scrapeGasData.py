#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import os

from scraper.EtherchainScraper import EtherchainScraper
from Config import Config
from DBManager import DBManager


configDir = os.path.dirname(os.path.realpath(__file__)) + "/config"

try:
    dbConfig = Config.readDB(configDir + "/db.yml")
except FileNotFoundError as e:
    dbConfig = False

if not dbConfig:
    print("No Database configuration found!")
    exit()

dbManager = DBManager.createDBManager(dbConfig['host'], dbConfig['dbName'])

scraper = EtherchainScraper(dbManager)

SLEEP_TIME = 10
scraper.run(SLEEP_TIME) # every 10 seconds

