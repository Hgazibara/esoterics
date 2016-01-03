#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import random

import esoterics.befunge


def run(code):
    memory = esoterics.befunge.Memory()
    memory.fill(code)

    pointer = esoterics.befunge.Pointer()

    interpreter = esoterics.befunge.Interpreter(memory, pointer)
    return interpreter.interpret()


class Interpreter(object):

    binary_operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div,
        '%': operator.mod
    }

    def __init__(self, memory, pointer):
        self.memory = memory
        self.pointer = pointer

    def interpret(self):
        stack = []
        output = []
        ascii_mode_active = False

        while True:
            cell = self.memory[self.pointer]
            command = cell.value

            if cell.is_empty():
                self.pointer.move()
                continue

            if ascii_mode_active:
                if command == '"':
                    ascii_mode_active = False
                else:
                    stack.append(ord(command))

            else:
                if command == '"':
                    ascii_mode_active = True

                elif command.isdigit():
                    stack.append(int(command))

                elif command in '+-*/%':
                    a, b = stack.pop(), stack.pop()
                    try:
                        stack.append(self.binary_operations[command](b, a))
                    except ZeroDivisionError as e:
                        stack.append(a)

                elif command == '!':
                    stack.append(int(not stack.pop()))

                elif command == '`':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b > a))

                elif command in '<>^v':
                    self.pointer.direction = command

                elif command == '?':
                    self.pointer.direction = '<>^v'[random.randint(0, 3)]

                elif command == '_':
                    a = stack.pop()
                    self.pointer.direction = '>' if a == 0 else '<'

                elif command == '|':
                    a = stack.pop()
                    self.pointer.direction = 'v' if a == 0 else '^'

                elif command == ':':
                    x = 0 if not stack else stack[-1]
                    stack.append(x)

                elif command == '\\':
                    a = stack.pop()
                    b = stack.pop() if stack else 0
                    stack.extend([a, b])

                elif command == '$':
                    stack.pop()

                elif command == '.':
                    output.append(str(stack.pop()))

                elif command == ',':
                    output.append(chr(stack.pop()))

                elif command == '#':
                    self.pointer.make_move()

                elif command == 'p':
                    y, x, v = stack.pop(), stack.pop(), stack.pop()
                    self.memory[y][x] = chr(v)

                elif command == 'g':
                    y, x = stack.pop(), stack.pop()
                    stack.append(ord(self.memory[y][x]))

                elif command == '@':
                    return ''.join(output)

            self.pointer.move()
