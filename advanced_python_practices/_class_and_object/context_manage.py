# -*- coding: utf-8 -*-
# @Author: gloomy
# @Date:   2016-11-19 21:43:03
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-19 22:47:59


# we could not take care of recycle the resources we occupy before when we use context-manage
with open('context_manage.py', 'r') as f:
	for line in f:
		print line
# f.close()
print '*' * 10 + 'end'


"""
summary:
we need to define the methods '__enter__','__exit__' of the instance if we want to realize context-manage.
the two methods refered above was called begin with 'with' and end apart.
"""