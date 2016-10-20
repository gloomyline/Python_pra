# -*- coding: utf-8 -*-
"""
@Time    : create on 10/20/2016 21:55
@Author  : Alan
@File    : history.py
@Software: PyCharm Community Edition
"""
import os
import pickle
from collections import deque
from random import randint

rdm_num = randint(0, 100)
queue = deque([], 5)
# load history
if os.path.exists('history'):
    queue = pickle.load(open('history'))


def guess(num):
    if num == rdm_num:
        print 'You got it!'
        return True
    if num < rdm_num:
        print '%d is less than rdm_num' % num
    if num > rdm_num:
        print '%d is greater than rdm_num' % num
    return False


while True:
    print '*' * 10
    input_line = raw_input('Please guess this num:')
    if input_line.isdigit():
        g_num = int(input_line)
        queue.append(g_num)
        if guess(g_num):
            # save queue into file named history
            pickle.dump(queue, open('history', 'w'))
            break
    elif input_line == 'history' or 'h?':
        # history
        for n in queue:
            print n,
        # CRLF
        print
