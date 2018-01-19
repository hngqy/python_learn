# -*-coding: utf-8 -*-

import urllib
import urllib2
import lxml.html as HTML

if __name__ == "__main__":
    # 此段代码的目的是为了爬取下边网页上的“更新时间”
    req_url = 'http://www.mumayi.com/android-81548.html'
    headers = {'User-Agent': '"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0"'}
    req = urllib2.Request(req_url, headers=headers)
    content = urllib2.urlopen(req, timeout=60).read()
    if isinstance(content, unicode):
        pass
    else:
        content = content.decode('utf-8')
    htmlSource = HTML.fromstring(content)
    print content
    retrans_content_tags = htmlSource.xpath(
        u'//div[@class="c"][4]/child::text()|//div[@class="c"][$_i]/a[position()>1]/child::text()')  #
    names = htmlSource.xpath(u'//ul[@class="istyle fl"]/li[3]/span')
    print names[0].text
    time = htmlSource.xpath(u'//ul[@class="istyle fl"]/li[3]/child::text()')
    print time[0]