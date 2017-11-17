#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests


class BaseApi:
    baseDomain = ""

    def __init__(self, api_key=False, api_secret=False):
        self.requests = requests
        self.api_key=api_key
        self.api_secret=api_secret
