# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:51:10 2017

@author: simon
"""

import threading
import time

class myThread(threading.Thread):
    exitFlag = 0
    
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    
    def run(self):
        print("starting:"+self.name)
        print_time(self.name,self.counter,5)
        print("Exit:"+self.name)
        pass
    
    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                threading.Thread.exit()
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))
            counter -= 1

thread = myThread(1,"test1",1)
thread2 = myThread(2,"test2",2)

thread.start()
thread2.start()
