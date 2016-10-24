# -*- coding: utf-8 -*-
"""
Created on 2016/10/24
@fn:
@author: Alan Wang
"""
import re

f = open('mongodb.log', 'r')
f_cont = f.read()
# style one
# res = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', f_cont)
# style two:name group
res = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', f_cont)
print res

f.close()

"""
如何调整字符串文本中文本的格式？

使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，
捕获每个部分的内容，在替换字符串中调整各个捕获组的顺序"""
