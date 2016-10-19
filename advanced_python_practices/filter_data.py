# -*- coding: utf-8 -*-
"""
@Time    : create on 10/19/2016 22:02
@Author  : Alan
@File    : filter_data.py
@Software: PyCharm Community Edition
"""

from random import randint
from datetime import datetime

# common
data = [1, 4, -3, -2, 5, 0, 9]

res = []
for num in data:
    if num >= 0:
        res.append(num)

print '迭代过滤负数后的列表', res

# advanced
l = [randint(-10, 10) for n in xrange(10)]
print '随机生成的包含10个整数的列表：', l
print 'filter函数方式'
fl = filter(lambda x: x >= 0, l)
print '过滤负数后的列表：', fl
print '列表解析方式'
print '过滤负数后的列表：', [y for y in l if y >= 0]

print '使用timeit方式在ipython中测试 使用列表解析执行时间更短'

print '---------------'

d = {x: randint(40, 100) for x in xrange(1, 21)}
print '随机生成包含20个同学的分数的字典', d
fd = {k: v for k, v in d.iteritems() if v >= 90}
print '筛选出分数高于90的同学的字典', fd

print '---------------'

s = set(data)
print '将列表转换成集合', s
fs = {x for x in s if x % 3 == 0}
print '筛选出能被3整除的子集', fs
