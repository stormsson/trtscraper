#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock

from TRTApi import TRTApi

from utils.dataproxy.TRTDataProxy import TRTDataProxy

class TestTRTDataProxy(unittest.TestCase):

    def test_init_sets_apiManager(self):
        proxy = TRTDataProxy(object())
        self.assertIsNotNone(proxy.api)


if __name__ == '__main__':
    unittest.main()