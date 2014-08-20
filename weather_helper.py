#!usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2013

@author: yilulu
'''
import weather
import ConfigParser
import sys
import time

from fetion import fetion
#from tools.misc import setlog

ERROR_TIME = 60


def send_weather_info(contact_list, extral_info):
    user = '15801481572 '  # 手机号
    passwd = 'j582033'  # 飞信密码
    f = fetion(user, passwd)
    f.login()

    cfg = ConfigParser.RawConfigParser()
    cfg.read(contact_list)
    cities = cfg.sections()

    for city in cities:
        contact_id_list = [id[1] for id in cfg.items(city)]
        count = 0
        while count < ERROR_TIME:
            try:
                msg = weather.get_weather_by_city(city) + "\n" + extral_info
                break
            except IndexError:
                log.info('Fetch failed, wait 60s')
                count += 1
                time.sleep(60)
        if count == ERROR_TIME:
            pass
            log.info('Fetch failed. City: %s', city)
            #TODO 发邮件通知一下
        else:
            try:
                if city == 'beijing':
                    f.send_tomyself(msg)
                for cid in contact_id_list:
                    status = f.send_msg(cid, msg)
                log.info('Send status: %s. City: %s', status, city)
            except Exception, e:
                log.exceptione('Send failed. City: %s.Err: %s', city, e)
                #TODO 发邮件通知一下


if __name__ == "__main__":
#    if len(sys.argv) > 1:
#        log_path = sys.argv[1]
#        log = setlog(filename=log_path, console=None)
#    else:
#        log = setlog()
#    log.info('Start')
    contact_list = 'contact_list1'
    extral_info = u"测试"
    try:
        send_weather_info(contact_list, extral_info)
    except Exception, e:
        log.exceptione(e)
    log.info('End')
