#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock

from utils.dataproxy.DBDataProxy import DBDataProxy
from DBManager import DBManager

class TestDBDataProxy(unittest.TestCase):
    # def setUp(self):
    #     self.mocked_db_manager = DBManager()



    def test_init_sets_dbManager(self):
        proxy = DBDataProxy(object())
        self.assertIsNotNone(proxy.dbManager)


    def test_calls_get_last_fund(self):
        proxy = DBDataProxy(object())



if __name__ == '__main__':
    unittest.main()