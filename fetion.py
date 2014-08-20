#!usr/bin/env python
# -*- coding: utf-8 -*-
import cookielib
import urllib
import urllib2
import time, re, json
import weather

class fetion():

    def __init__(self, phone_number, passwd):
        self.login_url = 'http://f.10086.cn/huc/user/space/login.do?m=submit&fr=space'
        self.url_msg = 'http://f.10086.cn/im/chat/sendMsg.action'
        self.token_url = "http://f.10086.cn/im/chat/toinputMsg.action?touserid="
        self.tomyself = 'http://f.10086.cn/im/user/sendMsgToMyselfs.action'
        self.phone_number = phone_number
        self.passwd = passwd

    def login(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        args = {'mobilenum':self.phone_number, 'password':self.passwd}
        post_args = urllib.urlencode(args)
        resp = opener.open(self.login_url, post_args)
        #print resp.read()
        self.opener = opener
        return opener

    def get_csrftoken(self, id_contact):
        time.sleep(5)
        token_url = self.token_url+id_contact
        print token_url
        resp = self.opener.open(token_url)
        s = resp.read()
        print s
        token = re.search(r'<postfield name="csrfToken" value="([a-z0-9]+)"/>', s).group(1)
        return token

    def send_msg(self, id_contact, msg):
        #id_contact 为飞信好友的一个联系号码，可以通过下面的show_contact_list得到好友信息，从而得知这个号码
        #
        token = self.get_csrftoken(id_contact)
        args = {'msg':msg.encode('utf8'), 'touserid':id_contact, 'csrfToken':token}
        post_args = urllib.urlencode(args)
        resp = self.opener.open(self.url_msg, post_args)
        return resp.read()

    def send_tomyself(self, msg):
        args = {'msg':msg.encode('utf8')}
        post_args = urllib.urlencode(args)
        resp = self.opener.open(self.tomyself, post_args)
        print resp.read()
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



if __name__ == "__main__":

    user = '15899746524'#手机号
    passwd = 'j582033'#飞信密码
    f = fetion(user, passwd)

    msg = u'test'
    #num = ',706239555'
    id_contact = "634800131"
    #    ,634800131
    f.login()
    #f.send_msg(id_contact, msg)
    f.send_tomyself(msg)


