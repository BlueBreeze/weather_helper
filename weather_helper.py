# -*- coding: utf-8 -*- 
'''
Created on Mar 25, 2013

@author: yilulu
'''
import fetion, weather
import ConfigParser, sys
from fetion import fetion

def send_weather_info(contact_list):

    user = ''#手机号
    passwd = ''#飞信密码
    f = fetion(user, passwd)
    
    msg = u'测试测试'
    #num = ',706239555'
    id_contact = '634800131,706239555'
    #    ,634800131
    f.login()

    cfg = ConfigParser.RawConfigParser()
    cfg.read(contact_list)
    cities = cfg.sections()

    for city in cities:
        contact_id_list =[ id[1] for id in cfg.items(city)]
        str_idcontact =  ",".join(contact_id_list)
        msg = weather.get_weather_by_city(city)
        print f.send_msg(str_idcontact, msg)
        
if __name__ == "__main__":   
    
    contact_list = 'contact_list'
    send_weather_info(contact_list)