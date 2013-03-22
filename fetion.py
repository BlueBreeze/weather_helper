# -*- coding: utf-8 -*- 
import cookielib
import urllib
import urllib2
import time, re, json

def login(login_url, phone_number, passwd):
    
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    args = {'t':int(time.time()), 'm':phone_number, 'pass':passwd}
    post_args = urllib.urlencode(args)
    resp = opener.open(login_url, post_args)
    print resp.read()  
    return opener
    
def send_msg(url_msg, opener, id_contact, msg):
    
    args = {'t':int(time.time()), 'msg':msg.decode('gbk').encode('utf-8'), 'touserid':id_contact}
    post_args = urllib.urlencode(args)
    resp = opener.open(url_msg, post_args)
    print resp.read()
    
def show_contact_list(url_show_list, opener, group_id):
    #这个groupid就是分组的组号按顺序0,1,2......
    #http://f.10086.cn/im5/index/contactlistView.action?fromUrl=&idContactList=4&t=1363847625762&_=1363847625762
    t = int(time.time())
    args = {'fromUrl':'', 'idContactList':group_id, 't':t , '_':t}
    post_args = urllib.urlencode(args)
    resp = opener.open(url_show_list, post_args)
    contact_list = resp.read()
    dict_contact = json.loads(contact_list)
    return dict_contact

def classify_frined(dict_contact):

    #查手机归属地http://shouji.duapp.com/phone.php 一个参数m
    for friend in dict_contact['contacts']:
        phone = friend['mobileNo']
        idContact = friend['idContact']
        flag = friend['basicServiceStatus']
         

if __name__ == "__main__":
    
    login_url = 'http://f.10086.cn/im5/login/loginHtml5.action'
    #url_logout = 'http://f.10086.cn//im/index/logoutsubmit.action'
    url_msg = 'http://f.10086.cn/im5/chat/sendNewGroupShortMsg.action'
    url_show_list = 'http://f.10086.cn/im5/index/contactlistView.action?fromUrl=&idContactList=4&t=1363847625762&_=1363847625762'
    user = ''
    password = ''
    loginstatus = '4' 
    msg = u'中文'
    group_id = '3'
    num=',706239555'
    #    ,634800131
    opener = login(login_url, user, password)
    send_msg(url_msg, opener, num, msg)
    #show_contact_list(url_show_list, opener, group_id)


