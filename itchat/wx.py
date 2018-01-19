# -*- coding:utf-8 -*-
import itchat
import time

def lc():
    print("Finash Login!")
def ec():
    print("exit")

itchat.auto_login(loginCallback=lc, exitCallback=ec)
time.sleep()
itchat.logout()    #强制退出登录