#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

from BaseOrderManager import BaseOrderManager

class LogOrderManager(BaseOrderManager):
    def buy(self, amount, price):
        try:
            logging.warning("Buying %s @ %s" % (amount, price))
        except Exception as e:
            raise e

        return True

    def sell(self, amount, price):
        try:
            logging.warning("Selling %s @ %s" % (amount, price))
        except Exception as e:
            raise e

        return True