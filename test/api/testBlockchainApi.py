#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import json
from unittest.mock import MagicMock
import datetime
import requests

from api.BlockchainApi import BlockchainApi

class TestBlockchainApi(unittest.TestCase):

    def setUp(self):
        self.api  = BlockchainApi()

    def test_stats_sanification(self):
        statsMockResponse = {
            "market_price_usd": 610.036975,
            "hash_rate": 1.8410989266292908E9,
            "total_fees_btc": 6073543165,
            "n_btc_mined": 205000000000,
            "n_tx": 233805,
            "n_blocks_mined": 164,
            "minutes_between_blocks": 8.2577,
            "totalbc": 1587622500000000,
            "n_blocks_total": 430098,
            "estimated_transaction_volume_usd": 1.2342976868108143E8,
            "blocks_size": 117490685,
            "miners_revenue_usd": 1287626.6577490852,
            "nextretarget": 431423,
            "difficulty": 225832872179,
            "estimated_btc_sent": 20233161880242,
            "miners_revenue_btc": 2110,
            "total_btc_sent": 184646388663542,
            "trade_volume_btc": 21597.09997288,
            "trade_volume_usd": 1.3175029536228297E7,
            "timestamp": 1474035340000
        }

        response = requests.Response()
        response.json = MagicMock(return_value=statsMockResponse)

        self.api.requests.get = MagicMock(return_value=response)

        result = self.api.getStats()

        self.assertTrue(result["date"])
        self.assertIsInstance(result["date"], str)


if __name__ == '__main__':
    unittest.main()