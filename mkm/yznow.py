# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""
每日游资买入股票
"""

if __name__ == "__main__":
    url="http://data.eastmoney.com/stock/hyyyb.html"
    executable_path = r"C:\DEV\tool\python2.7\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS(executable_path=executable_path,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    driver.get(url)
    time.sleep(3)

    pages = driver.find_elements_by_xpath("//div[@id='PageCont']/a")
    driver.find_elements_by_xpath("")
    print str(len(pages))
    print pages[len(pages)-2].text
