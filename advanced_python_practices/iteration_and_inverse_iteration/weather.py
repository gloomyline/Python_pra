# -*- coding: utf-8 -*-
"""
@Time    : create on 10/21/2016 00:47
@Author  : Alan
@File    : weather.py
@Software: PyCharm Community Edition
"""
from time import time

import requests
from collections import Iterable, Iterator


# http://wthrcdn.etouch.cn/weather_mini?city=北京 获取城市天气接口
# def get_weather(city):
#     r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#     if r.status_code == 200:
#
#         # print r.json()['data']['forecast'][0]
#         data = r.json()['data']['forecast'][0]
#         return '%s: %s , %s' % (city, data['low'], data['high'])
#
# print get_weather(u'厦门')
# print get_weather(u'合肥')


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        if r.status_code == 200:
            # TODO: reference data in weather_data.json
            data = r.json()['data']['forecast'][0]
            return '%s: %s , %s' % (city, data['low'], data['high'])


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


# [u'北京', u'上海', u'广州', u'杭州', u'合肥', u'厦门', u'南京']
def show_weather(cities):
    for city_weather in WeatherIterable(cities):
        print time(), ':', city_weather


show_weather([u'北京', u'上海', u'广州', u'杭州', u'合肥', u'厦门', u'南京'])
