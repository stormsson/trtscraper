#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import twitter

class TwitterScraper:
    def __init__(self, consumer_key, consumer_secret, token, token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

        self.token = token
        self.token_secret = token_secret

        self.api = twitter.Api(consumer_key,
                  consumer_secret,
                  token,
                  token_secret)

        # print(self.api.VerifyCredentials())

    def GetUserTimeline(self, screen_name, count=20):
        return self.api.GetUserTimeline(screen_name=screen_name, count=count)


