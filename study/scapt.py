import re
import urllib
import urllib2
#coding=utf-8

def getHtml(baseurl):
    #baseUrl='http://www.taobao.com'
    try:
        urllib2.urlopen()
        response = urllib2.urlopen(baseurl)
        response.read()

    except BaseException:
        print   "get data is fail!!!"
    return html

def cbk(a,b,c):
    per=100*a*b/c
    if per>100:
        per=100
    print '%.2f%%' % per
def getImage(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

url="https://tieba.baidu.com/p/2460150866"
html = getHtml(url)
imglist = getImage(html)

x=0
for imgurl in imglist:
    urllib.urlretrieve(imgurl,'./tmp/%s.jpg' %x,cbk)
    print imgurl
    x=x+1
