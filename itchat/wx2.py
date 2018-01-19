# -*- coding:utf-8 -*-
import itchat
import time

itchat.auto_login()
users = itchat.search_friends(name=u"Ph-任刚林")
username = users[0]['UserName']
print username
for i in range(100):
    itchat.send_msg("hello world",toUserName=username)