#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import esoterics.tests.test_case
import esoterics.brainfuck


class TestTokenizer(esoterics.tests.test_case.TestCase):
    def test_tokenize_produces_sequence_of_tokens(self):
        tokens = esoterics.brainfuck.tokenize('[->+<]')
        self.assertIsSequence(tokens)


if __name__ == '__main__':
    unittest.main()
