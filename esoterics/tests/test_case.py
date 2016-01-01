#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation
"""

import unittest


class TestCase(unittest.TestCase):

    def assertIsSequence(self, actual, msg=''):
        try:
            __ = (__ for __ in actual)
        except TypeError:
            self.fail(msg)