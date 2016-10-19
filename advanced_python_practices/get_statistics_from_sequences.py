# -*- coding: utf-8 -*-
"""
@Time    : create on 10/19/2016 23:38
@Author  : Alan
@File    : get_statistics_from_sequences.py
@Software: PyCharm Community Edition
"""

from random import randint

data = [randint(0, 20) for _ in xrange(30)]
print '生成30个随机的0到20之间的数的列表', data

c = dict.fromkeys(data, 0)
print '初始化字典', c

for x in data:
    c[x] += 1

# after get statistics
print '统计后的字典', c

# sort c
# sorted(c, cmp=lambda c.x, c.y: )
