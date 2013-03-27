# -*- coding: utf-8 -*- 
import cookielib
import urllib
import urllib2
import time, re, json
import weather

class fetion():
    
    def __init__(self, phone_number, passwd):
        self.login_url = 'http://f.10086.cn/im5/login/loginHtml5.action'
        self.url_msg = 'http://f.10086.cn/im5/chat/sendNewGroupShortMsg.action'
        #self.url_show_list = 'http://f.10086.cn/im5/index/contactlistView.action?fromUrl=&idContactList=4&t=1363847625762&_=1363847625762'
        self.phone_number = phone_number
        self.passwd = passwd
        
    def login(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        args = {'t':int(time.time()), 'm':self.phone_number, 'pass':self.passwd}
        post_args = urllib.urlencode(args)
        resp = opener.open(self.login_url, post_args)
        #print resp.read()
        self.opener = opener
        return opener
    
    def send_msg(self, id_contact, msg):
        #id_contact 为飞信好友的一个联系号码，可以通过下面的show_contact_list得到好友信息，从而得知这个号码
        args = {'t':int(time.time()), 'msg':msg.decode('gbk').encode('utf-8'), 'touserid':id_contact}
        post_args = urllib.urlencode(args)
        resp = self.opener.open(self.url_msg, post_args)
        #print resp.read()
        return resp.read()
    
    def show_contact_list(self, opener, group_id):
        #这个groupid就是分组的组号按顺序0,1,2......
        #http://f.10086.cn/im5/index/contactlistView.action?fromUrl=&idContactList=4&t=1363847625762&_=1363847625762
        t = int(time.time())
        args = {'fromUrl':'', 'idContactList':group_id, 't':t , '_':t}
        post_args = urllib.urlencode(args)
        resp = self.opener.open(self.url_show_list, post_args)
        contact_list = resp.read()
        self.dict_contact = json.loads(contact_list)
        return dict_contact

    def classify_frined(self):

        #查手机归属地http://shouji.duapp.com/phone.php 一个参数m
        for friend in self.dict_contact['contacts']:
            phone = friend['mobileNo']
            idContact = friend['idContact']
            flag = friend['basicServiceStatus']
         

if __name__ == "__main__":
    
    user = ''#手机号
    passwd = ''#飞信密码
    f = fetion(user, passwd)
    
    msg = u'测试测试'
    #num = ',706239555'
    id_contact = ',706239555'
    #    ,634800131
    f.login()
    print f.send_msg(id_contact, msg)


