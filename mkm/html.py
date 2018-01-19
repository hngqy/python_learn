import urllib2

class html():

    def __init__(self,url):
        self.url = url

    def getContent(self):
        #print self.url
        request = urllib2.Request(url=self.url)
        response = urllib2.urlopen(request)
        return response.read()
