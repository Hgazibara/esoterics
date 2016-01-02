#!/usr/bin/env python
# -*- coding: utf-8 -*-

import esoterics.brainfuck


def run(code, input_values):
    tokens = esoterics.brainfuck.tokenize(code)
    memory = esoterics.brainfuck.Memory()
    pointer = esoterics.brainfuck.Pointer()
    interpreter = Interpreter(tokens, input_values, memory, pointer)
    return interpreter.interpret()


class Interpreter(object):

    def __init__(self, tokens, input_values, memory, pointer):
        self.tokens = tokens
        self.inputs = input_values
        self.memory = memory
        self.pointer = pointer

        self.token_index = 0
        self.output = []

        self.__commands = {
            '>': self.increment_pointer,
            '<': self.decrement_pointer,
            '+': self.increment_value,
            '-': self.decrement_value,
            ',': self.read_input,
            '.': self.store_output,
            '[': self.enter_branch,
            ']': self.leave_branch
        }

    def interpret(self):
        total_tokens = len(self.tokens)

        while self.token_index < total_tokens:
            self.process(self.tokens[self.token_index])
            self.token_index += 1

        return ''.join(self.output)

    def process(self, token):
        self.__commands[token.command](token)

    def increment_pointer(self, token):
        self.pointer.up()
        if len(self.memory) == self.pointer.position:
            self.memory.expand()

    def decrement_pointer(self, token):
        self.pointer.down()

    def increment_value(self, token):
        cell = self.current_cell()
        cell.increment()

    def decrement_value(self, token):
        cell = self.current_cell()
        cell.decrement()

    def read_input(self, token):
        cell = self.current_cell()
        cell.value = ord(self.inputs.next())

    def store_output(self, token):
        cell = self.current_cell()
        self.output.append(chr(cell.value))

    def enter_branch(self, token):
        cell = self.current_cell()
        if cell.is_empty():
            self.token_index = token.next

    def leave_branch(self, token):
        cell = self.current_cell()
        if not cell.is_empty():
            self.token_index = token.next

    def current_cell(self):
        return self.memory.cell(self.pointer.position)
