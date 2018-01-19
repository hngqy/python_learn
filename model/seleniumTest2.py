# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

executable_path=r"C:\DEV\tool\python2.7\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=executable_path)
driver.get("http://www.baidu.com/")

size = driver.find_element_by_name("wd").size

print size
# 尺寸: {'width': 500, 'height': 22}

news = driver.find_element_by_xpath("//div[@id='u1']/a[1]").text
print news
# 文本: 新闻

href = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('href')
name = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('name')
print href, name
# 属性值: http://www.hao123.com/ tj_trhao123

location = driver.find_element_by_xpath("//div[@id='u1']/a[3]").location
print location
# 坐标: {'y': 19, 'x': 498}

print driver.current_url
# 当前链接: https://www.baidu.com/
print driver.title
# 标题: 百度一下， 你就知道

result = location = driver.find_element_by_id("su").is_displayed()
print result
# 是否可见: True