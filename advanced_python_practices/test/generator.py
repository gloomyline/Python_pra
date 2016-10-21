# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""


def fn():
    print 'in fn, 1'
    yield 1

    print 'in fn, 2'
    yield 2

    print 'in fn, 3'
    yield 3

g = fn()
print g.next()
print g.next()
print g.next()

print '生成器对象类似迭代器对象，具有抽象接口next()'

print '*' * 10
g1 = fn()
for i in g1:
    print i

print '同样生成器对象也是一个可迭代对象'

print '*' * 10

print '生成器对象的迭代器是它自身', g1.__iter__() is g1
