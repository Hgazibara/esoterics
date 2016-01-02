#!/usr/bin/env python
# -*- coding: utf-8 -*-


def tokenize(code):
    loop_starts = []
    tokens = []

    for position, command in enumerate(code):
        if command == '[':
            loop_starts.append(position)

        if command == ']':
            loop_start = loop_starts.pop()
            tokens.append(Token(command, loop_start))
            tokens[loop_start].next = position
        else:
            tokens.append(Token(command, position + 1))

    return tokens


class Token(object):

    def __init__(self, command, next_position):
        self.command = command
        self.next = next_position
