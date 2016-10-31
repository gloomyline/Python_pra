# -*- coding: utf-8 -*-
"""
@Time    : create on 10/31/2016 20:23
@Author  : Alan
@File    : csv_rw.py
@Software: PyCharm Community Edition
"""
import csv
import os
from urllib import urlretrieve

from itertools import islice

"""
使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写"""

if not os.path.exists('pingan.csv'):
    """
    第一个参数url
    第二个参数下载后保存的文件名
    """
    urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')
    print 'download complete'
else:
    print 'it exists'

_csv = open('pingan.csv', 'r')

# 查看下载后的文件内容的前10行
for l in islice(_csv, 0, 10, None):
    print l,
print

# 将2016年的成交额大于50000000的记录写到'pingan2.csv'中
with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        header = reader.next()
        writer.writerow(header)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) > 50000000:
                writer.writerow(row)
        print 'write complete'
print 'end'
