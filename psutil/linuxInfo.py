# -*- coding:utf-8 -*-

import psutil

men = psutil.virtual_memory()
print men
print men.total
print men.used

cpu = psutil.cpu_times(percpu=True)

#逻辑核心数
print psutil.cpu_count()
#物理核心数
print psutil.cpu_count(logical=False)

#磁盘信息
print psutil.disk_partitions()  #获取磁盘完整信息
print psutil.disk_usage("C:\\APP\\") #磁盘使用信息

#网络信息
print psutil.net_io_counters()

