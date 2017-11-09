#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

from BaseOrderManager import BaseOrderManager

class LogOrderManager(BaseOrderManager):
    def buy(self, amount, price):
        logging.warning("Buying %s @ %s" % (amount, price))
        return True

    def sell(self, amount, price):
        logging.warning("Selling %s @ %s" % (amount, price))
        return True