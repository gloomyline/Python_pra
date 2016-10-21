# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""


class FloatRange(object):
    def __init__(self, start, stop, step=0.1):
        self.start = start
        self.stop = stop
        self.step = step

# def __iter__(self):
#     l = int((self.stop - self.start) / self.step)
#     for i in xrange(l):
#         yield self.start + i * self.step

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

for f in FloatRange(1, 2.2, 0.11):
    print f

print '*' * 10

for f in reversed(FloatRange(1, 2.2, 0.11)):
    print f
