#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yaml

class Config:

    @staticmethod
    def readDB(path):
        with open(path) as f:
            dbConfig = yaml.safe_load(f)
        return dbConfig

    def readFile(path):
        with open(path) as f:
            cfg = yaml.safe_load(f)
        return cfg