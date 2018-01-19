# -*- coding: utf-8 -*-
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://data.eastmoney.com/stock/lhb.html"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
urldata = response.read()
type = sys.getdefaultencoding()
data = urldata.decode('gb2312').encode(type)


