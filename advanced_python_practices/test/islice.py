# coding: utf-8
from itertools import islice


f = open('mongod.log')
for line in islice(f, 0, None):
    print line

f.close()

print u'完成对文件内容切片'
print '*' * 20

l = [x for x in xrange(20)]
print l
for n in islice(iter(l), 5, 10, 2):
    print n,
print
print u'完成对迭代器切片'