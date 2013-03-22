# -*- coding: utf-8 -*- 
'''
Created on Mar 22, 2013

@author: yilulu
'''
import urllib2
import lxml.html as HTML

def get_weather_by_city(city):
    
    beijing = "http://tianqi.2345.com/beijing/54511.htm"
    chengdu = "http://tianqi.2345.com/chengdu/56294.htm"
    hangzhou = "http://tianqi.2345.com/hangzhou/58457.htm"
    changsha = "http://tianqi.2345.com/changsha/57687.htm"
    wuhan = "http://tianqi.2345.com/wuhan/57494.htm"
    
    dict_weather = {'beijing':beijing,\
                   'chengdu':chengdu,\
                   'hangzhou':hangzhou,\
                   'changsha':changsha,\
                   'wuhan':wuhan
                   }
    
    weather_url = dict_weather[city]
    html = urllib2.urlopen(weather_url).read()
    html = html.decode('gbk', 'ignore')
    print html
    root = HTML.document_fromstring(html)
    
    date = root.xpath("//li[@class=\'week-detail-now\']")[0].text_content()
    PM2d5 = root.xpath("//h3[@id=\'AQIL\']/em")[0].text_content()
    AQLI = root.xpath("//h3[@id=\'AQIL\']/b")[0].text_content()
    lifeindex = root.xpath("//ul[@class=\'lifeindex\']/li")
    umbrella = lifeindex[0].text_content()
    clothes = lifeindex[2].text_content()
    air = lifeindex[5].text_content()
    print date, umbrella, clothes, air
    print 'PM2.5指数：'+PM2d5, '空气质量：'+AQLI
 
if __name__ == "__main__":   
    city = 'chengdu'
    get_weather_by_city(city)