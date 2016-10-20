# -*- coding: utf-8 -*-
"""
@Time    : create on 10/20/2016 22:57
@Author  : Alan
@File    : iteration_obj_and_iterator_obj.py
@Software: PyCharm Community Edition
"""
from random import randint

# iteration include list and str
l = [randint(0, 10) for _ in xrange(5)]
print l
s = 'abcdef'
print s

# iterator <- iter(iteration)
t = iter(l)
print t
for i in xrange(len(l)):
    print t.next()
