#!/usr/bin/env python
# -*- coding: utf-8 -*-

UNMATCHED_LOOP_START_ERROR = 'No loop end "]" for loop start "[" at position {position}'
UNMATCHED_LOOP_END_ERROR = 'No loop start "[" for loop end "]" at position {position}'


def tokenize(code):
    loop_starts = []
    tokens = []

    for position, command in enumerate(code):
        if command == '[':
            loop_starts.append(position)

        if command == ']':
            if not loop_starts:
                raise TokenizerError(UNMATCHED_LOOP_END_ERROR.format(position=position))
            loop_start = loop_starts.pop()
            tokens.append(Token(command, loop_start))
            tokens[loop_start].next = position
        else:
            tokens.append(Token(command, position + 1))

    if loop_starts:
        raise TokenizerError(UNMATCHED_LOOP_START_ERROR.format(position=loop_starts[-1]))

    return tokens


class Token(object):

    def __init__(self, command, next_position):
        self.command = command
        self.next = next_position


class TokenizerError(Exception):
    pass
