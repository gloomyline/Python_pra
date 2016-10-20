# -*- coding: utf-8 -*-
"""
@Time    : create on 10/19/2016 23:38
@Author  : Alan
@File    : get_statistics_from_sequences.py
@Software: PyCharm Community Edition
"""

import re
from random import randint
from collections import Counter

data = [randint(0, 20) for _ in xrange(30)]
print '生成30个随机的0到20之间的数的列表', data

c = dict.fromkeys(data, 0)
print '初始化字典', c

for x in data:
    c[x] += 1

# after get statistics
print '迭代字典统计后的字典', c

# sorted c by v
c_value_list = []
for k, v in c.iteritems():
    c_value_list.append(v)
print sorted(c_value_list, reverse=True)

print '----------'

c1 = Counter(data)
print '使用Counter类统计后的字典', c1

print '出现频率最高的3项', c1.most_common(3)

txt = open('get_statistics_from_sequences.txt').read()
str_l = re.split('\W+', txt)
c2 = Counter(str_l)
print c2
print c2.most_common(10)
