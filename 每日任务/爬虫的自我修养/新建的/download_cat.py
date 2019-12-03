#---调用这个包的模块
import urllib.request

        #---open这里传入的字符串
response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()


        #相当于执行下两句
        ##rep = urllib.request.Request("http://placekitten.com/g/200/300")
        ##response = urllib.request.urlopen(rep)

#---他会返回你的这个url地址
response.geturl()
#---他会返回服务器返回的一些时间  地址端口之类的
##response.info()
##print(response,info())
#---wb二进制文件打开  with open as f不需要繁琐的打开关闭文件
with open("cat_200_300.jpg","wb")as f:
#----f.write添加指定字符
    f.write(cat_img)
    
