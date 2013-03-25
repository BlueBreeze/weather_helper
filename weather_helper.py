'''
Created on Mar 25, 2013

@author: yilulu
'''
import fetion, weather
import ConfigParser

def send_weather_info(contact_list):
    
    url_msg = 'http://f.10086.cn/im5/chat/sendNewGroupShortMsg.action'
    login_url = 'http://f.10086.cn/im5/login/loginHtml5.action'
    phone_number = ''# ÷ª˙∫≈
    passwd = ''#∑…–≈√‹¬Î
    cfg = ConfigParser.RawConfigParser()
    cfg.read(contact_list)
    cities = cfg.sections()

    opener = fetion.login(login_url, phone_number, passwd)
    for city in cities:
        contact_id_list =[ id[1] for id in cfg.items(city)]
        str_idcontact =  ",".join(contact_id_list)
        msg = weather.get_weather_by_city(city)
        print fetion.send_msg(url_msg, opener, str_idcontact, msg)
        
if __name__ == "__main__":   
    
    contact_list = 'contact_list'
    send_weather_info(contact_list)