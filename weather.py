#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import json
import sys
from threading import Thread

city_code = {
    'beijing': {'code':54511, 'name':u'北京'},
    'chengdu': {'code':56294, 'name':u'成都'},
    'hangzhou': {'code':58457, 'name':u'杭州'},
    'changsha': {'code':57687, 'name':u'长沙'},
    'wuhan': {'code':57494, 'name':u'武汉'},
    'fuzhou':{'code':58847, 'name':u'福州'},
    'ningbo':{'code':58465, 'name':u'宁波'},
    'shaoyang':{'code':57766,'name':u'邵阳'},
    'zibo':{'code':54830, 'name':u'淄博'},
    'linzi':{'code':60815, 'name':u'临淄'}
}

def get_weather_by_city(city):
    base_url = "http://tianqi.2345.com"
    code = city_code[city]['code']
    weather_url = "%s/%s/%s.htm" % (base_url, city, code)
    root = BeautifulSoup(requests.get(weather_url).content)

    li_today = root.findAll('li', {'class':'week-detail-now'})[0]
    day = li_today.findAll('b')[0].text
    night = li_today.findAll('b')[1].text

    Temp = li_today.find('i').findAll('font')
    low = Temp[0].text
    high = Temp[1].text

    degress = low + "~" + high

    lifeindex = root.findAll('ul', {'class':'lifeindex'})[0].findAll('li')
    umbrella = lifeindex[4].text
    clothes = lifeindex[3].text

    #空气质量
    GMT_FORMAT = "new_%a %b %d %Y %H:%M:%S GMT 0800="
    arg_time = time.strftime(GMT_FORMAT, time.localtime(time.time()))
    pm25_url = "http://tianqi.2345.com/t/shikuang/%s.js?%s" % (code, arg_time)
    weather_info = json.loads(requests.get(pm25_url).content.split("=")[-1].replace(";", ""))['weatherinfo']
    wkeys = weather_info.keys()
    if 'pm25' in wkeys:
        pm25 = u"PM2.5指数为：" + str(weather_info['pm25'])
        level = weather_info['lv_hint']
        idx = weather_info['idx']
    else:
        pm25 = u"PM2.5值无数据"
        level = u"无"
        idx = 0

    idx_info = u"空气质量指数为：%s %s" % (str(idx), level)
    date_format = "%b %d %Y"
    date = time.strftime(date_format, time.localtime(time.time()))
    weather = [city_code[city]['name'], date, degress, day, night, pm25, idx_info, umbrella, clothes]
    return "\n".join(weather)

def print_weather(city):
    print get_weather_by_city(city)
    print '--------------------------'

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        print get_weather_by_city('beijing')
    else:
        params = sys.argv[1:]
        for city in params:
            Thread(target = print_weather, args = [city]).start()
