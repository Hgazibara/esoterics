#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class Input(object):

    __metaclass__ = abc.ABCMeta

    def __iter__(self):
        return self

    @abc.abstractmethod
    def next(self):
        pass


class PredefinedInput(Input):

    def __init__(self, input_values):
        self.input_values = iter(input_values)

    def next(self):
        return next(self.input_values)


class ConsoleInput(Input):

    def __init__(self, message=''):
        self.message = message

    def next(self):
        try:
            input_value = raw_input('{message}:'.format(message=self.message))
            return input_value
        except EOFError:
            raise StopIteration
