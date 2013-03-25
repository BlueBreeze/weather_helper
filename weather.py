# -*- coding: utf-8 -*- 
'''
Created on Mar 22, 2013

@author: yilulu
'''
import urllib2
import lxml.html as HTML
import time, json

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
    #print html
    root = HTML.document_fromstring(html)
    
    day = root.xpath("//li[@class=\'week-detail-now\']/b")[0].text_content()
    night = root.xpath("//li[@class=\'week-detail-now\']/b")[1].text_content()
    degress = root.xpath("//li[@class=\'week-detail-now\']/i")[0].text_content()

    print day, night, degress
    lifeindex = root.xpath("//ul[@class=\'lifeindex\']/li")
    umbrella = lifeindex[0].text_content()
    clothes = lifeindex[2].text_content()
    air = lifeindex[5].text_content()
    print umbrella, clothes, air
    
    #空气质量
    GMT_FORMAT = "new_%a %b %d %Y %H:%M:%S GMT 0800="
    arg_time = time.strftime(GMT_FORMAT, time.localtime(time.time()))
    pm25_url = "http://tianqi.2345.com/t/shikuang/"+weather_url.split('/')[-1].split('.')[0]+".js?"+arg_time
    weather_info = json.loads(urllib2.urlopen(pm25_url).read().split("=")[-1].replace(";",""))['weatherinfo']
    pm25 = "PM2.5 =" + weather_info['pm25']
    idx = u"空气质量指数为：" + weather_info['idx']
    print pm25, idx
    weather = [degress, day, night, pm25, idx, air, umbrella, clothes]
    return " ".join(weather)
 
if __name__ == "__main__":   
    city = 'wuhan'
    get_weather_by_city(city)