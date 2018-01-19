#!/user/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

hostname="localhost"
username="root"
passwd="123456"
database="gp"

db = MySQLdb.connect(hostname,username,passwd,database)

cursor = db.cursor()

sql = """
    create table test(
        id int,
        name varchar(16),
        age int
    )
"""

insert_sql ="""
    insert into test values(1,'simon',28)
"""
try:
    cursor.execute(insert_sql)
    db.commit()
    data = cursor.fetchone()
except :
    db.rollback()
print ("create sql:%s"%data)