#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests


class BaseApi:
    baseDomain = ""

    def __init__(self):
        self.requests = requests
