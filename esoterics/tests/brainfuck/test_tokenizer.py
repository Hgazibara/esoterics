#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import esoterics.tests.test_case
import esoterics.brainfuck


class TestTokenizer(esoterics.tests.test_case.TestCase):
    def test_tokenize_produces_sequence_of_tokens(self):
        tokens = esoterics.brainfuck.tokenize('[->+<]')
        self.assertIsInstanceOfTokens(tokens)

    def test_token_contains_position_of_next_token(self):
        tokens = esoterics.brainfuck.tokenize('[->+<]')
        token = tokens[1]
        self.assertEqual(token.next, 2)

    def test_open_loop_token_contains_position_of_close_loop_token(self):
        tokens = esoterics.brainfuck.tokenize('[->+<]')
        token = tokens[0]
        self.assertEqual(token.next, 5)


if __name__ == '__main__':
    unittest.main()
