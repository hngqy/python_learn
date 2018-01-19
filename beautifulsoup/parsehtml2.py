# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import os

def getHtml(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    header = {"User-Agent":user_agent}
    try:
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request)
        content = response.read()
    except urllib2.HTTPError as e:
        print e
        exit()
    except urllib2.URLError as e:
        print e.reason
        exit()
    return content.decode("utf-8")

if __name__ == '__main__':
    # 创建目录
    path = "./qiubai"
    if not os.path.exists(path):
        os.mkdir(path)

    regex = re.compile('<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
    for cnt in range(1,35):
        url = "https://www.qiushibaike.com/textnew/page/"+str(cnt)+"/?s=5028231"
        content = getHtml(url)
        soup_packetpage = BeautifulSoup(content,"lxml")
        items = soup_packetpage.find_all("div",class_="content")
        for item in items:
            print  item.span.string