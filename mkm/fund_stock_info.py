# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import traceback
from dblink import dblink
import multiprocessing
import sys
import json
reload(sys)
sys.getdefaultencoding()
sys.setdefaultencoding("utf-8")

def getstockinfo(fundcode,fundname):
    try:
        executable_path = r"C:\DEV\tool\python2.7\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe"
        driver = webdriver.PhantomJS(executable_path=executable_path,
                                     service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
        print "begin ......"+str(fundcode)
        url = "http://fund.eastmoney.com/{fundcode}.html"
        url = url.format(fundcode=fundcode)
        driver.get(url)
        time.sleep(3)
        trs = driver.find_elements_by_xpath('//div[@class="poptableWrap"]/table[@class="ui-table-hover"]/tbody/tr')
        index = 0
        print "len:"+str(len(trs))
        out="[ "
        for tr in trs:
            if len(str(tr.text).strip()) != 0:
                if index > 0 and index <= len(trs):
                    tds = tr.find_elements_by_xpath("./td")
                    gpcodestr = tds[0].find_element_by_xpath("./a").get_attribute("href")
                    gpcode = str(gpcodestr).split("/")[3].split(".")[0][2:]
                    #print str(fundcode)+"------"+tds[0].text+"----"+tds[1].text+"---"+gpcode
                    rowJson = "{\"fundcode\": \"" + str(fundcode) + "\",\"fundname\": \"" + fundname + "\" ,\"gpnum\":" \
                              + str(index) + ",\"gpcode\":\"" + str(gpcode) + "\",\"gpname\":\"" + tds[0].text + "\",\"gprate\":\"" + str(tds[1].text) + "\"}"

                    # rowinfo.append(fundcode)
                    # rowinfo.append(fundname)
                    # rowinfo.append(index)
                    # rowinfo.append(gpcode)
                    # #股票名字
                    # rowinfo.append(tds[0].text)
                    # #股票比例
                    # rowinfo.append(tds[1].text)
                    out = out+ rowJson+","
            index = index +1
        out=out.strip(",")+" ]"
        print out
        return str(out)
    except Exception,e:
        print "getstockinfo Exception:"+e
        traceback.print_exc()

    return ""
if __name__ == "__main__":
    ip = 'localhost'
    username = 'root'
    passwd = '123456'
    database = 'gp'
    db = dblink(ip, username, passwd, database)
    conn = db.getConnect()
    fundSql = "select fundcode,fundname from gp.fund_main_info where length(fundname) >0"
    fundcodes = db.executQuery(conn,fundSql)
    index = 1
    pool = multiprocessing.Pool(processes=10)
    gp_result_info=[]

    for fc in fundcodes:
        if index > 0:
            print str(fc)+"---"+str(index)
            ###获取股票信息
            gp_result_info.append(pool.apply_async(getstockinfo,(fc[0],fc[1])))
        if index % 10 == 0:
            time.sleep(120)
        index=index+1
    pool.close()
    pool.join()

    ##处理结果数据
    for res in gp_result_info:
        if len(res.get())>0:
            datas = json.loads(res.get())
            for row in datas:
                insertFundSql = "insert into gp.fund_stock_basic(fundcode,fundname,gpnum,gpcode,gpname,gprate) values('{fundcode}','{fundname}','{gpnum}','{gpcode}','{gpname}','{gprate}')"
                insertFundSql = insertFundSql.format(fundcode=row["fundcode"],fundname=row["fundname"],gpnum=str(row["gpnum"]),gpcode=str(row["gpcode"]),gpname=row["gpname"],gprate=str(row["gprate"]))
                print str(row["fundcode"])+"---"+row["fundname"]+"-----"+str(row["gpnum"])+"-----"+str(row["gpcode"])+row["gpname"]+"-----"+str(row["gprate"])
                print insertFundSql
                db.update(conn,insertFundSql)
    print "end"
    #getstockinfo("161910","test")