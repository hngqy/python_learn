import urllib2
import urllib
import os
from bs4 import BeautifulSoup

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
if __name__ == "__main__":
    url="http://www.qu.la/book/16431/6944450.html"
    content = getHtml(url)
    #print  content
    bs = BeautifulSoup(content,"lxml")
    titlediv = bs.find_all("div",_class="con_top")
    print titlediv
