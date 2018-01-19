# coding=UTF-8
import urllib2
import urllib
import re



"""抓取淘宝mm信息"""
class Spider(object):

    def __init__(self):
        self.siteUrl="https://mm.taobao.com/json/request_top_list.htm"

    def getUrlInfo(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read().decode('gbk')
        except Exception as e:
            html = None
            print e
        return html

    def getPage(self,pageIndex):
        url = self.siteUrl+"?page="+str(pageIndex)
        return self.getUrlInfo(url)

    def getContent(self,html):
        if not html:
            print '没有获取到数据'
        else:
            reg = '<div class="list-item".*?pic-word.*?<a class="lady-name.*?href="(.*?)".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>'
            pattern = re.compile(reg,re.S)
            items = re.findall(pattern,html)
            for item in items:
                print item[0],item[1],item[2],item[3]

spider = Spider()
html = spider.getPage(1)
spider.getContent(html)

