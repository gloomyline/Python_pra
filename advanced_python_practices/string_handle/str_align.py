# -*- coding: utf-8 -*-
"""
Created on 2016/10/24
@fn:
@author: Alan Wang
"""

d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trillinear": 40,
    "farclip": 477
}

# s.ljust() s.rjust() s.center()

s = 'abc'
print 'leftjustfied', s.ljust(10, '*')
print 'rightjustfied', s.rjust(10, '*')
print 'centerjustfied', s.center(10, '*')

print '*' * 10

print format(s, '<10')
print format(s, '>10')
print format(s, '^10')

print '*' * 10

kl = d.keys()
ms = max(kl)
print len(ms)
for k, v in d.iteritems():
    print format(k, '<' + str(len(ms))), ':', str(v)

print 'method two:'
for k in d:
    print k.ljust(max(map(len, kl))), ':', d[k]

print 'method two is better'
