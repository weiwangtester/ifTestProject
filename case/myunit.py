#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import case.base as base


class MyTest(unittest.TestCase):
    def setUp(self):
        self.session = base.Base.get_base_session()
        return

    def tearDown(self):
        base.Base.set_base_session(self.session)
        return

    @classmethod
    def setUpClass(cls):
        return

    @classmethod
    def tearDownClass(cls):
        return
