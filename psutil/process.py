# -*- coding:utf-8 -*-

import psutil

pids = psutil.pids() #列出所有进程号

pout=""
for pid in pids:

    p = psutil.Process(pid) #列出一个进程
    if pid == 7344:
        print p
        pout="进程名:",p.name()+"绝对路径:",p.cwd()+"进程状态:",p.status() +\
            "进程内存利用率:",p.memory_percent()
        print pout
