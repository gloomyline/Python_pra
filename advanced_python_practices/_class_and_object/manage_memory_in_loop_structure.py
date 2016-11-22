# -*- coding: utf-8 -*-
# @Author: gloomy
# @Date:   2016-11-22 21:26:05
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-22 22:13:09


"""
question:
garbage collector collects unused objects by applying to counter in Python.
But there are circulatory references in some loop structure such as tree and map.
For example,parent node references son node,at the same time,son node alse referencs parent node.
If we delete the parent and son,collector won't collect the garbage at once.
Therefor,how we could solve this question about memory mangement.
Let's talk about this.
"""
import gc
import weakref

class Data(object):
	"""docstring for Data"""
	def __init__(self, value, owner):
		self.value = value
		self.owner = weakref.ref(owner)

	def __str__(self):
		return '%s\'s data, value is %s' % (self.owner(), self.value)

	def __del__(self):
		print 'in Data.__del__'

class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.data = Data(value, self)

	def __del__(self):
		print 'in Node.__del__'

node = Node(100)
del node
# gc.collect()
raw_input('wait...')

"""
Standard lib 'weakref' can create an object which could access to another object but not add the count of references.
"""
		
		