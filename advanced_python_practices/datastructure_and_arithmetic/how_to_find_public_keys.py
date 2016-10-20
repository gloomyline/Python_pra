# -*- coding: utf-8 -*-
"""
Created on 2016/10/20
@fn:
@author: Alan Wang
"""


from random import randint, sample

print 'generate random dicts'
dicts_l = []
for _ in xrange(3):
    d = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 7))}
    dicts_l.append(d)
print dicts_l

print 'use iter to find public key'
res = []
for k in dicts_l[0].keys():
    if k in dicts_l[1] and k in dicts_l[2]:
        res.append(k)
print res
print '----------------'

print 'use mixed set'
print dicts_l[0].viewkeys() & dicts_l[1].viewkeys() & dicts_l[2].viewkeys()
print '----------------'

print 'use reduce'
m = map(dict.viewkeys, dicts_l)
print m
res1 = reduce(lambda x, y: x & y, m)
print res1
