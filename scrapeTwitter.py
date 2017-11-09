#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import os
import re
import datetime

from Config import Config
from DbManager import DbManager
from utils.TwitterScraper import TwitterScraper
from utils.WhaleCallsAnalyzer import WhaleCallsAnalyzer


WCAnalyzer = WhaleCallsAnalyzer()
twitterDateFormat = '%a %b %d %H:%M:%S %z %Y'

def scrapeWhaleCalls(scraper, dbManager):
    max_tweet = 10
    tweets = scraper.GetUserTimeline(screen_name="whalecalls", count=max_tweet)

    records_to_insert = []

    tw_ids = [ t.id_str for t in tweets ]
    found_ids_cursor = dbManager.findWhaleCallsByIds(tw_ids)

    found_ids = [ item["id_str"] for item in found_ids_cursor]

    del found_ids_cursor



    for t in tweets:
        if t.id_str not in found_ids:

            record = WCAnalyzer.analyze(t.text)


            if record:
                record['date'] = datetime.datetime.strptime(t.created_at, twitterDateFormat)
                record['text'] = t.text
                record['id_str'] = t.id_str
                records_to_insert.append(record)

    return records_to_insert

configDir = os.path.dirname(os.path.realpath(__file__)) + "/config"

try:
    dbConfig = Config.readDB(configDir + "/db.yml")
except FileNotFoundError as e:
    dbConfig = False

if not dbConfig:
    print("No Database configuration found!")
    exit()

dbManager = DbManager(dbConfig['host'], dbConfig['dbName'])

try:
    apiConfig = Config.readDB(configDir + "/api.yml")
except FileNotFoundError as e:
    apiConfig = False


if not apiConfig or not apiConfig['twitter']:
    print("No API configuration found!")
    exit()

twitterScraper = TwitterScraper(
        apiConfig['twitter']['consumer_key'],
        apiConfig['twitter']['consumer_secret'],
        apiConfig['twitter']['token'],
        apiConfig['twitter']['token_secret']
    )


while True:
    new_posts = scrapeWhaleCalls(twitterScraper, dbManager)
    if len(new_posts):
        dbManager.saveWhaleCalls(new_posts)
    time.sleep(60)
