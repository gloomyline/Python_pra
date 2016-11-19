# -*- coding: utf-8 -*-
# @Author: gloomy
# @Date:   2016-11-19 15:36:45
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-19 21:37:27
import sys


class Player(object):
	"""docstring for Player"""
	def __init__(self, uid, name, status = 0, level = 1):
		self.uid = uid
		self.name = name
		self.status = status
		self.level = level
		
class Player2(object):
	"""docstring for Player2"""
	__slots__ = ['uid', 'name', 'status', 'level']
	def __init__(self, uid, name, status = 0, level = 1):
		self.uid = uid
		self.name = name
		self.status = status
		self.level = level

# dir() this method could return the properties of the object which was preferenced
p1 = Player('00001', 'Alan')
p2 = Player2('00002', 'Jerry')
# print dir(p1)
# print dir(p2)
print set(dir(p1)) - set(dir(p2))
print p1.__dict__

# p1 has no attribute 'x'
# print p1.x

# assign the attribute 'x' to p1 dynamically
p1.x = 123
print p1.x

# add the attribute 'y' to the attribute '__dict__' of p1
p1.__dict__['y'] = 1234
print p1.y

# delete attribute of p1 by deleting the attribute in '__dict__'
del p1.__dict__['x']

# p1 has no attribute 'x' because of that it was deleted before
# print p1.x

# get the memory which is occupied by '__dict'
print sys.getsizeof(p1.__dict__)

# we could not add any attributes to p2 except those we declared before by defining '__slots'
# p2.x = 123

"""
summary:
define the property called '__slots__' which is used to declare the lists of instantiation properties.
"""