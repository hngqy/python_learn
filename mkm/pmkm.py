# -*- coding=UTF-8 -*-

from html import html
from dblink import dblink
from lxml import etree
import sys
import codecs

url='http://fund.eastmoney.com/data/fundranking.html'

if __name__  == '__main__':
    htmlObject = html(url)
    rootContent = htmlObject.getContent()
   # print rootContent
    #f = codecs.open("funder.html")
    #content = f.read()
    text = unicode(rootContent, "utf-8")
    selector = etree.HTML(text)
    lista = selector.xpath('//div[class="fvbox left"]/a/@href')
    for a in lista :
        print a
 
