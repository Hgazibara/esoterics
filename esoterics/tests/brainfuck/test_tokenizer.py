#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import esoterics.brainfuck
import esoterics.tests.test_case
from esoterics.tests.helpers import brainfuck_data


class TestTokenizer(esoterics.tests.test_case.TestCase):
    def test_tokenize_produces_sequence_of_tokens(self):
        tokens = esoterics.brainfuck.tokenize(brainfuck_data.some_code())
        self.assertIsInstanceOfTokens(tokens)

    def test_token_contains_position_of_next_token(self):
        tokens = esoterics.brainfuck.tokenize(brainfuck_data.some_code())
        token_position = brainfuck_data.token_position()
        self.assertEqual(tokens[token_position].next, token_position + 1)

    def test_open_loop_token_contains_position_of_close_loop_token(self):
        tokens = esoterics.brainfuck.tokenize(brainfuck_data.some_code())
        token = tokens[brainfuck_data.open_loop_position()]
        self.assertEqual(token.next, brainfuck_data.close_loop_position())

    def test_close_loop_token_contains_positions_of_open_loop_token(self):
        tokens = esoterics.brainfuck.tokenize('[->+<]')
        token = tokens[brainfuck_data.close_loop_position()]
        self.assertEqual(token.next, brainfuck_data.open_loop_position())


if __name__ == '__main__':
    unittest.main()
