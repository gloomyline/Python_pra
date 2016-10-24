# -*- coding: utf-8 -*-
"""
Created on 2016/10/24
@fn:
@author: Alan Wang
"""

pl = ['abc', 123, 456, 'xyz']

print 'method one:'
s = ''
for x in pl:
    x = str(x)
    s += x
print s

print '*' * 10

print 'method two:S.join()'
# (str(x) for x in pl) -> generator object
s1 = ''.join((str(x) for x in pl))
print s1
