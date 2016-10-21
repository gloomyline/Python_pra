# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""


l = [1, 2, 3, 4, 5]
print l[::-1]
print '*' * 10

l.reverse()
print '修改了原来的序列', l
print '*' * 10

print '生成了新的序列，资源浪费', l[::-1]

print '*' * 10, 'use reversed() to generate listreverseiterator'
print reversed(l)

for x in reversed(l):
    print x,


