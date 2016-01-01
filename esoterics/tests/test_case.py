#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from esoterics.brainfuck import Token


class TestCase(unittest.TestCase):

    def assertIsInstanceOfTokens(self, actual, msg=''):
        self.assertIsSequence(actual, msg)

        for token in actual:
            if not isinstance(token, Token):
                self.assertIsInstance(token, Token)
                break

    def assertIsSequence(self, actual, msg=''):
        try:
            (__ for __ in actual)
        except TypeError:
            self.fail(msg)
