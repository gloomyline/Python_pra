# -*- coding: utf-8 -*-
# @Author: gloomy
# @Date:   2016-11-19 21:57:37
# @Last Modified by:   gloomy
# @Last Modified time: 2016-11-19 22:57:47
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque


class TelnetClient(object):
	"""docstring for TelnetClient"""
	def __init__(self, addr, port=23):
		
		self.addr = addr
		self.port = port
		self.tn = None

	def start(self):
		# move these into method '__enter__'
		# self.tn = Telnet(self.addr, self.port)
		# self.history = deque()

		# user
		t = self.tn.read_until('login: ')
		stdout.write(t)
		user = stdin.readline()
		self.tn.write(user)

		# password
		t = self.tn.read_until('password: ')
		if t.startswith(user[:-1]): 
			t = t[len(user) + 1:]
		stdout.write(t)
		self.tn.write(stdin.readline())

		t = self.tn.read_until('$ ')
		stdout.write(t)
		while True:
			uinput = stdin.readline()
			if not uinput:
				break
			self.history.append(uinput)
			self.tn.write(uinput)
			t = self.tn.read_until('$ ')
			stdout.write(t[len(uinput) + 1:])

	def cleanup(self):
		self.tn.close()
		self.tn = None
		with open('../telnet_client_histories/' + self.addr + '_history.txt', 'w') as f:
			f.writelines(self.history)

	def __enter__(self):
		self.tn = Telnet(self.addr, self.port)
		self.history = deque()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print 'In __exit__'
		self.cleanup()
		return True
		

# client = TelnetClient('127.0.0.1')
# print '\nstart...'
# client.start()
# print '\ncleanup'
# client.cleanup()
with TelnetClient('127.0.0.1') as client:
	client.start()
print 'END'