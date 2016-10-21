# -*- coding: utf-8 -*-
"""
@Time    : create on 10/21/2016 20:58
@Author  : Alan
@File    : concurrent_and_chain_in_iteration.py
@Software: PyCharm Community Edition
"""
from itertools import chain
from random import randint

print 'concurrent'
cls = []
for _ in xrange(4):
    cls.append([randint(40, 100) for _ in xrange(40)])
print u'一个班级的语文、数学、英语、体育成绩', cls

total = []
for c, m, e, s in zip(cls[0], cls[1], cls[2], cls[3]):
    total.append(c + m + e + s)
print u'每个学生的总分列表', total

print '*' * 10

print 'chain'
count = 0
csls = []
for _ in xrange(4):
    csls.append([randint(40, 100) for _ in xrange(randint(35, 45))])
print u'四个班级所有同学语文成绩的列表', csls
for s in chain(csls[0], csls[1], csls[2], csls[3], ):
    if s >= 90:
        count += 1
print u'四个班级中所有分数大于等于90的数量', count
