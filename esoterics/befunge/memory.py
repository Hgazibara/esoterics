#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Memory(object):

    MAX_X = 25
    MAX_Y = 80

    def __init__(self):
        self.cells = [[Cell()] * self.MAX_Y for _ in xrange(self.MAX_X)]

    def fill(self, code):
        for i, row in enumerate(code):
            for j, cell in enumerate(row):
                self.cells[i][j] = cell

    def __getitem__(self, pointer):
        return self.cells[pointer.x][pointer.y]


class Cell(object):

    def __init__(self, value=None):
        self.value = value


class Pointer(object):

    directions = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = '>'

    def move(self):
        x, y = self.directions[self.direction]
        self.x = (self.x + x) % Memory.MAX_X if (self.x + x) >= 0 else Memory.MAX_X + x
        self.y = (self.y + y) % Memory.MAX_Y if (self.y + y) >= 0 else Memory.MAX_Y + y
