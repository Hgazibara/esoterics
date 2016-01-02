#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from esoterics.tests import test_case
import esoterics.brainfuck


class TestCell(test_case.TestCase):

    def test_increment_increments_value_by_one(self):
        cell = esoterics.brainfuck.Cell()
        old_value = cell.value
        cell.increment()
        self.assertEqual(cell.value, old_value + 1)

    def test_incrementing_maximum_values_drops_value_to_default(self):
        cell = esoterics.brainfuck.Cell()
        cell.value = esoterics.brainfuck.Cell.MAX_VALUE
        cell.increment()
        self.assertEqual(cell.value, cell.EMPTY_VALUE)

    def test_decrement_decrements_value_by_one(self):
        cell = esoterics.brainfuck.Cell()
        target_value = 10
        cell.value = target_value
        cell.decrement()
        self.assertEqual(cell.value, target_value - 1)

    def test_decrementing_default_value_increases_value_to_maximum(self):
        cell = esoterics.brainfuck.Cell()
        cell.value = esoterics.brainfuck.Cell.EMPTY_VALUE
        cell.decrement()
        self.assertEqual(cell.value, cell.MAX_VALUE)


if __name__ == '__main__':
    unittest.main()
