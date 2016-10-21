# -*- coding: utf-8 -*-
"""
Created on 2016/10/21
@fn:
@author: Alan Wang
"""
from time import time

import requests


def get_cities_weather(cities):
    for city in cities:
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        print time(), '%s : %s %s' % (city, data['low'], data['high'])

get_cities_weather([u'北京', u'上海', u'广州', u'杭州', u'合肥', u'厦门', u'南京'])
