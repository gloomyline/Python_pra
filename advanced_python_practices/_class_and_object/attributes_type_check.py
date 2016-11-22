# -*- coding: utf-8 -*-
# @Author: Alan
# @Date:   2016-11-22 20:21:35
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-22 21:25:09


class Attr(object):
	"""docstring for Descriptor"""
	def __init__(self, name, type_):
		self.name = name
		self.type_ = type_

	def __get__(self, instance, cls):
		# print 'in __get__', instance, cls
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		# print 'in __set__', instance
		if not isinstance(value, self.type_):
			raise TypeError('expected an %s' % self.type_)
		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		# print 'in __del__'
		del instance.__dict__[self.name]

class Person(object):
	"""docstring for A"""
	name = Attr('name', str)
	age = Attr('age', int)
	height = Attr('height', float)

p = Person()
p.name = 'Bob'
print p.name
# p.age = '12'

"""
summary:
implement to check the type of attributes by using descriptor
'__get__, __set__, __delete__'
"""