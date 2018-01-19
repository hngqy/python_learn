# -*- coding=UTF-8 -*-

from html import html
from dblink import dblink
from lxml import etree
import sys
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import time

reload(sys)
sys.getdefaultencoding()
sys.setdefaultencoding("utf-8")
url='http://fund.eastmoney.com/data/fundranking.html'
fundurl="http://fund.eastmoney.com/002612.html"

if __name__  == '__main__':
    ip = 'localhost'
    username = 'root'
    passwd = '123456'
    database = 'gp'
    print "begin: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    executable_path = r"C:\DEV\tool\python2.7\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS(executable_path=executable_path,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_id("showall").click()
    time.sleep(3)
    lis=driver.find_elements_by_xpath("//ul[@id='types']/li")
    fundindex = 0

    for li in lis :
        fundindex = fundindex+1
        li.click()
        time.sleep(3)
        if len(str(li.text).strip()) !=0:
            print li.text
    fundtype = 8
    i = 0
    lis[9].click()
    time.sleep(3)
    print lis[9].text
#    tbody = driver.find_element_by_xpath("//table[@id='dbtable']/tbody")
#    print tbody.text
    trs = driver.find_elements_by_xpath("//table[@id='dbtable']/tbody/tr")
    fundLists = []
    trIndex = 0
    tsql="select fundtype from gp.fund_main_info where fundcode='{fundcode}'"
    usql="update fund_main_info set fundtype='{fundtype}' where fundcode='{fundcode}'"
    sql="insert into gp.fund_main_info values('{fundcode}','{fundname}','{netvalue}','{weekrate}','{month1rate}','{month3rate}','{month6rate}','{year1rate}','{year2rate}','{year3rate}','{currentrate}','{totalrate}','{fundtype}')"
    print "while begin: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for tr in trs :
        tds = tr.find_elements_by_xpath("./td")
        tdIndex = 0
        rowLists = []
        for td in tds :
            if trIndex>-1:
                if(tdIndex ==2 or tdIndex ==3  or tdIndex ==5 or tdIndex ==8 or tdIndex ==9 or tdIndex ==10 or tdIndex ==11 or tdIndex ==12 or tdIndex ==13 or tdIndex ==14 or tdIndex ==15 or tdIndex ==16 ):
                    if(str(td.text).find("-") == -1):
                        rowLists.append(td.text)
                    else:
                        rowLists.append("")
                tdIndex = tdIndex + 1
                #print str(td.text).strip().strip("\n")
        if trIndex > -1:
            rowLists.append(str(fundtype))
            fundLists.append(rowLists)
        #print str(tdIndex)+"***********************"
        trIndex = trIndex+1
    print "while end: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db = dblink(ip, username, passwd, database)
    conn = db.getConnect()
    for fund in fundLists:
        ft = db.findOne(conn,tsql.format(fundcode=fund[0]))
        if ft == None:
            insertSql = sql.format(fundcode=fund[0],fundname=fund[1],netvalue=fund[2],weekrate=fund[3],month1rate=fund[4],month3rate=fund[5],month6rate=fund[6],year1rate=fund[7],year2rate=fund[8],year3rate=fund[9],currentrate=fund[10],totalrate=fund[11],fundtype=fund[12])
            db.update(conn, insertSql)
            print insertSql
        else:
            if str(ft[0]).find(str(fundtype)) == -1 :
                print str(ft[0])
                insertSql = usql.format(fundtype=str(str(ft[0])+","+str(fundtype)),fundcode=fund[0])
                db.update(conn, insertSql)
                print insertSql







