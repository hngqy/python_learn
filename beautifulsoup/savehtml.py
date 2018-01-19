import urllib2
import urllib
import os
from bs4 import *

def getHtml(url):
    headers = ""
    try :
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
    except urllib2.URLError as e:
        print e.reason
        exit()
    except urllib2.HTTPError as e:
        print e.reason
        exit()
    return  content.encode("utf-8")

def testBeautifulSour(conetent):
    print "hello world"
    soup = BeautifulSoup(content,"lxml")
    print soup.title.string
    print soup.p
    print soup.div
    print soup.find_all("a")
    print soup.find(id="content")

if __name__ == "__main__":
    url="http://www.qu.la/book/16431/6944450.html"
    content = getHtml(url)

    testBeautifulSour(content)
