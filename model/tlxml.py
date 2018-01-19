# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:53:55 2017

@author: simon
"""
from lxml import etree


import requests


url='http://www.baidu.com'
html = requests.get(url).content.decode('utf-8')
#print html
selector = etree.HTML(html)
al=selector.xpath("//div/a/@href")
for a in al:
    print a

