# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""


class PrimeNumbers(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime_num(self, num):
        if num < 2:
            return False
        for k in xrange(2, num):
            if num % k == 0:
                return False
        return True

    def __iter__(self):
        for n in xrange(self.start, self.end + 1):
            if self.is_prime_num(n):
                yield n

for p in PrimeNumbers(2, 100):
    print p
