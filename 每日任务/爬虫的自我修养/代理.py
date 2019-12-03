#----代理
import urllib.request

url = "http://www.whatismtip.com.tw"

proxy_support = urllib.request.ProxyHandler({"http":"123.139.85.101 "})
opener.addheaders = [{("User-Adent","")}]

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)


response = urllib.request.urlopen(url)

html = response.read().decode("utf-8")

print(html)
