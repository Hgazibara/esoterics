#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation
"""

def tokenize(code):
    return [Token(command, position + 1) for position, command in enumerate(code)]


class Token(object):

    def __init__(self, command, next_position):
        self.command = command
        self.next = next_position
