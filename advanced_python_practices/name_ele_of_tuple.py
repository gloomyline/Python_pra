# -*- coding: utf-8 -*-
"""
@Time    : create on 10/19/2016 22:48
@Author  : Alan
@File    : name_ele_of_tuple.py
@Software: PyCharm Community Edition
"""

from collections import namedtuple

# ('Alan', 23, 'male', '1211071880@qq.com')
# ('Pepa', 34, 'female', '1473853554@qq.com')
# ('James', 31, 'male', 'james007spy@gmail.com')

# define constant
"""
NAME = 0
AGE = 1
GENDER = 2
EMAIL = 3
"""
NAME, AGE, GENDER, EMAIL = xrange(4)

student = ('Alan', 23, 'male', '1211071880@qq.com')

# name
print student[NAME]

# age
if student[AGE] >= 30:
    print student[AGE]

# gender
if student[GENDER] == 'female':
    print student[GENDER]

print '-------------'

Student = namedtuple('Student', ['name', 'age', 'gender', 'email'])
print Student.__doc__

# instantiate with args or keywords
s = Student('Alan', 23, 'male', email='1211071880@qq.com')
print s
print s.name, s.age, s.gender, s.email, s[0], s[1]

# unpack like regular tuple
name, age, gender, email = s
print name, age

# convert to dictionary
d = s._asdict()
print d.__doc__
print d
print d['name'], d['age']

# convert from dictionary
print Student(**d)

# _replace() is like str.replace() but targets named fields
s1 = s._replace(name='Pepa', age=34, gender='female', email='1473853554@qq.com')
print s1

# every namedtuple is subclass of tuple
print isinstance(s, tuple), isinstance(s1, tuple)
