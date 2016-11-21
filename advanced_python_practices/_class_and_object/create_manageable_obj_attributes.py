# -*- coding: utf-8 -*-
# @Author: Alan
# @Date:   2016-11-21 19:55:03
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-21 20:13:52
from math import pi


class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius
		
	def getRadius(self):
		return round(self.radius, 2)

	def setRadius(self, value):
		if not isinstance(value, (int, long, float)):
			raise ValueError('wrong type.')
		self.radius = float(value)

	def getArea(self):
		return self.radius ** 2 * pi

	R = property(getRadius, setRadius)

c = Circle(3)
print c.getArea()

# c.radius = 'abc'
# print c.radius * 2
# c.setRadius('abc')

print c.R
c.R = pi
# c.R = '12'
print c.R

"""
create manageable attributes by using method 'property','fget/fset/fdel' are correspond with properties access.
"""