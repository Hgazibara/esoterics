#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Memory(object):

    MAX_X = 25
    MAX_Y = 80

    def __init__(self):
        self.cells = [[None] * self.MAX_Y for _ in xrange(self.MAX_X)]


class Pointer(object):

    def __init__(self):
        self.x = 0
        self.y = 0
