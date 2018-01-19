#coding=utf-8
import MySQLdb
import time
from lxml import etree
from dblink import dblink
from html import html
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def testSql():
    ip = 'localhost'
    username = 'root'
    passwd = '123456'
    database = 'gp'
    db = dblink(ip, username, passwd, database)
    tsql="select fundtype,fundname from gp.fund_main_info where fundcode={fundcode}"
    tsql=tsql.format(fundcode="000176")
    conn = db.getConnect()
    data = db.findOne(conn,tsql)
    print data[1]
    db.close(conn)



def testHtml():
    url = "http://www.baidu.com"
    h = html(url=url)
    content = h.getContent()
    selctor = etree.HTML(content)
    div = selctor.xpath('//div[@class="qrcode-text"]/p/b/text()')
    for d in div :
        print d

if __name__ == '__main__':
    testSql()
