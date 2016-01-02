#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Memory(object):

    MAX_SIZE = 30000

    def __init__(self):
        self.cells = [Cell()]

    def cell(self, index):
        return self.cells[index]

    def expand(self):
        self.cells.append(Cell())

    def __len__(self):
        return len(self.cells)


class Cell(object):

    MAX_VALUE = 255
    EMPTY_VALUE = 0

    def __init__(self):
        self.value = self.EMPTY_VALUE

    def increment(self):
        self.value = (self.value + 1) % (self.MAX_VALUE + 1)

    def decrement(self):
        self.value = self.MAX_VALUE if self.value == self.EMPTY_VALUE else self.value - 1

    def is_empty(self):
        return self.value == self.EMPTY_VALUE


class Pointer(object):

    def __init__(self):
        self.position = 0

    def up(self):
        self.position = min(Memory.MAX_SIZE, self.position + 1)

    def down(self):
        self.position = max(0, self.position - 1)
