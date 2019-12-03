#第一种方法实在Response对象生成之前   我们先设置好 然后把他作为参数传递进去


#第二种方法啊




import urllib.request
        #---调用这个包里的这个模块里的这个open函数读取这个网址
s = urllib.request.urlopen("http://www.baidu.com")
        #---使用read函数把这个获取到的网页读出来
html = s.read()
html =html.decode("utf-8")
print(html)
