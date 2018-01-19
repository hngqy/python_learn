import urllib2
import urllib

url = "http://www.baidu.com"
data={}
data['username']='aaa'
data['password']='123456'

print  data
print '-----------------------------'
value = urllib.urlencode(data)
print value
re = urllib2.urlopen(url)
txt = re.read()
print txt