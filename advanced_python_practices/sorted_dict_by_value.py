# -*- coding: utf-8 -*-
"""
Created on 2016/10/20
@fn:
@author: Alan Wang
"""


from random import randint

d = {x: randint(40, 100) for x in 'xyzabc'}
print d

print 'test----------:'
sd = sorted(d)
print d

print iter(d)
print list(iter(d))

print '--------------:'


print 'use zip()-----:'
# t = zip(d.values(), d.keys())
# use itervalues(), iterkeys() instead of above in order to save RAM
t = zip(d.itervalues(), d.iterkeys())
print t

st = sorted(t, None, None, True)
print st

print '--------------:'

print 'use key args of function sorted'
t1 = d.items()
print t1

st1 = sorted(t1, key=lambda x: x[1], reverse=True)
print st1
print '--------------:'

