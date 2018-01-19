#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

#获取数据库连接
db = MySQLdb.connect("localhost","root","123456","sakila")
#cursor操作获取游标
cursor = db.cursor()
#使用execute方法执行sql
cursor.execute("select VERSION()")
#使用fetchone获取第一条数据
data = cursor.fetchone()
print ("database version %s"%data)
db.close()