# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""
from itertools import islice

l = [x for x in xrange(20)]
print l

iterator = iter(l)

for x in islice(iterator, 5, 10):
    print x,
print
print '*' * 10

for x in iterator:
    print x,

print
print '*' * 10
