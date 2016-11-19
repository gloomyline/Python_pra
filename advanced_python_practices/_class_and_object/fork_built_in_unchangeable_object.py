# -*- coding: utf-8 -*-
# @Author: Alan
# @Date:   2016-11-19 15:11:54
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-19 15:34:02


class IntTuple(tuple):
	"""my tuple that could filter positive int number"""
	def __new__(cls, iterable):
		g = (x for x in iterable if isinstance(x, int) and x > 0)
		return super(IntTuple, cls).__new__(cls, g)
		
	def __init__(self, iterable):
		# before
		print self
		super(IntTuple, self).__init__(iterable)
		# after


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print t

"""
summary:
define the class IntTuple inherited built-in tuple,
realize the method called '__new__',
modify the action of instantiation of the IntTuple"""		