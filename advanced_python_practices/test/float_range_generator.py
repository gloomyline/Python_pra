# -*- coding: utf-8 -*-
"""
@Time    : create on 10/21/2016 20:21
@Author  : Alan
@File    : float_range_generator.py
@Software: PyCharm Community Edition
"""
from itertools import islice


class FloatRange(object):
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n <= self.stop:
            yield n
            n += self.step

    def __reversed__(self):
        n = self.stop
        while n >= self.start:
            yield n
            n -= self.step


for f in FloatRange(1.2, 3.0, 0.11):
    print f,

print
print '*' * 10

for f in reversed(FloatRange(1.2, 3.0, 0.11)):
    print f,

print
print '*' * 10

for f in islice(FloatRange(1.2, 3.0, 0.12), 4, 10):
    print f,

print
