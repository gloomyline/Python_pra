# -*- coding: utf-8 -*-
"""
@Time    : create on 10/20/2016 21:13
@Author  : Alan
@File    : how_to_keep_dict_ordered.py
@Software: PyCharm Community Edition
"""
from collections import OrderedDict
from random import randint
from time import time

print 'built_in dict:'

d = {}
d['Alan'] = (1, 15)
d['Michael'] = (2, 20)
d['Bob'] = (3, 23)
d['Leo'] = (4, 34)
for k in d:
    print k
print '-' * 10

print 'OrderedDict:'

d1 = OrderedDict()
d1['Alan'] = (1, 15)
d1['Michael'] = (2, 20)
d1['Bob'] = (3, 23)
d1['Leo'] = (4, 34)
for k in d1:
    print k
print '-' * 10

print 'simulate OrderedDict'

start = time()
players = list('ABCDEFGH')
res = OrderedDict()
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start
    res[p] = (i + 1, end - start)
print res
print '-' * 10

# run above in ipython
"""
>? 1
1 H 1.5039999485
>? 2
2 E 2.61099982262
>?
3 B 3.58599996567
>?
4 A 4.45799994469
>?
5 G 5.69000005722
>?
6 F 6.21099996567
>?
7 C 6.78499984741
>?
8 D 7.38100004196
OrderedDict([('H', (1, 1.503999948501587)), ('E', (2, 2.610999822616577)), ('B', (3, 3.5859999656677246)), ('A', (4, 4.45799994468689)), ('G', (5, 5.690000057220459)), ('F', (6, 6.210999965667725)), ('C', (7, 6.784999847412109)), ('D', (8, 7.38100004196167))])
----------
In[2]: res['H']
Out[9]:
(1, 1.503999948501587)
In[3]: res['G']
Out[10]:
(5, 5.690000057220459)
In[4]: res['A']
Out[11]:
(4, 4.45799994468689)"""
