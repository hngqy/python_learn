# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:32:16 2017

@author: simon
"""

import tthread
import time

def print_time(threadName,t):
    count=0
    while count < 5:
        time.sleep(t)
        count = count+1 
        print("%s: %s" % (threadName,time.ctime()))

try:
    tthread.start_new_thread(print_time, ("aa", 2))
except:
    print "error"

while 1:
    pass

    