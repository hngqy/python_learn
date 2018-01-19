# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:12:12 2017

@author: simon
"""

import multiprocessing
import time

def process(num):
    time.sleep(num)
    print "Process:"+str(num)
    
if __name__ == "__main__":
    
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print("cpu count:" + str(multiprocessing.cpu_count()))
    
    for p in multiprocessing.active_children():
        print("process name:"+p.name+" id:"+str(p.pid))