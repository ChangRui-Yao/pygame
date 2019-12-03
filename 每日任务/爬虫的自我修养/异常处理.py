import urllib.request
import urllib.error

            #--在这里访问一个不存在的网址
req = urllib.request.Request("http://dddd//ddddd.com")

try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
    
