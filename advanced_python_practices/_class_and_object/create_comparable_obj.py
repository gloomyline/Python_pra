# -*- coding: utf-8 -*-
# @Author: Alan
# @Date:   2016-11-21 20:14:57
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-21 21:47:34
from functools import total_ordering
from abc import ABCMeta, abstractmethod
from math import pi


@total_ordering
class Shape(object):
	"""docstring for Shape"""
	@abstractmethod
	def area(self):
		pass

	def __lt__(self, obj):
		print 'in __lt__'
		if not isinstance(obj, Shape):
			raise TypeError('object is not Shape.')
		return self.area() < obj.area()

	def __eq__(self, obj):
		print 'in __eq__'
		if not isinstance(obj, Shape):
			raise TypeError('object is not Shape.')
		return self.area() == obj.area()

class RectAngle(Shape):
	"""docstring for RectAngle"""
	def __init__(self, width, height):
		
		self.width = width
		self.height = height
		
	def area(self):
		return round(self.width * self.height, 2)

class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius
		
	def area(self):
		return round(self.radius ** 2 * pi, 2)

rect1 = RectAngle(5, 3)
rect2 = RectAngle(4, 4)
circle = Circle(3)

# print rect1 < 'rect2' # r1.__lt__ (r2)
print rect1 <= rect2
print rect1 > rect2
print circle > rect2
# print circle > 1

"""
summary:
we need to implement methods '__lt__, __le__, __gt__, __ge__, __eq__, __ne__', when we overload Comparison operators.
It is excellect to use decorator 'total_ordering' in 'functools' lib of standard libs.
"""