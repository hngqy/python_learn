# -*- coding=UTF-8 -*-

from html import html
from dblink import dblink
from lxml import etree
import sys
import codecs
from pyquery import PyQuery as pq

url='http://fund.eastmoney.com/data/fundranking.html'

if __name__  == '__main__':
    htmlObject = html(url)
    rootContent = htmlObject.getContent()
    print rootContent
    #text = unicode(rootContent,'gb2312')
    #text = unicode(rootContent, "utf-8")
    doc = pq(rootContent)
    lis = doc('.types #types li')
    print lis
