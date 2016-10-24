# -*- coding: utf-8 -*-
"""
Created on 2016/10/24
@fn:
@author: Alan Wang
"""
import re
import string

"""
字符串strip(),lstrip(),rstrip(),去掉字符串两端字符
删除单个固定位置的字符，可以使用切片+拼接方式
字符串replace()方法或正则表达式re.replace()删除任意位置字符
字符串translate()方法，可以同时删除多种不同字符"""

s = '    abc   123     '
print s.strip()
print s.lstrip()
print s.rstrip()

s1 = '---abc++'
print s1.strip('-+')

print '*' * 10

s2 = 'abc:123'
print s2[:3] + s2[4:]

print '*' * 10

s3 = '\tabc\t123\txyz'
print s3.replace('\t', '')
print s3

s4 = '\tabc\t123\rxyz\opq\r'
print re.sub(r'[\t\r\\]', '', s4)

print '*' * 10

# str.translate()
s5 = 'abc1230123xyz'
trans_table = string.maketrans('abcxyz', 'xyzabc')
print s5.translate(trans_table)

s6 = 'abc\t123'
print s6.translate(None, '\t')

# unicode.translate()
u = u'ni\u0301 ha\u030co, chi\u0304 fa\u0300n'
print u

u1 = u'ní hǎo, chī fàn'
print u1

print u1.translate(dict.fromkeys([0x0301, 0x030c, 0x0304, 0x0300]))
