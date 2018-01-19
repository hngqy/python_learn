# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:09:37 2017

@author: simon
"""


import time
from multiprocessing import Process
import multiprocessing

class myProcess(Process):
    
    def __init__(self,loop):
        Process.__init__(self)
        self.loop = loop
    
    def run(self):
        for count in range(self.loop):
            #time.sleep(1)
            print("process id :"+self.pid)

if __name__ == "___main__":
    for i in range(2,5,1):
        p = myProcess(i)
       # p.daemon = True
        p.start()
        #p.join()
    print "Main process End"
