"""
#定义啊要保存的图片路径
#调用文件下载的函数




"""
import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


def downlowd_image(img_url,file_name):
    try:
        #根据url地址请求网络资源
        response_data = urllib.request.urlopen(img_url)
        #在本地保存文件，准备保存
        with open(file_name,"wb") as file:
            while True:
                #读取返回的网络资源（循环）
                file_data = response_data.read(1024)
                #判断读到的文件不为空
                if file_data:
                    #把读取的资源写入到本地文件
                    file.write(file_data)
                else:
                    break
                    #异常捕获
    except Exception as e:
        print("文件%s下载失败" % file_name)
    else:
        print("文件%s下载成功" % file_name)
def main():
    #定义啊要保存的图片路径
    img_url1 = "http://placekitten.com/g/200/300"
    img_url2 = "http://placekitten.com/g/400/600"
    img_url3 = "http://placekitten.com/g/500/700"
    #调用下载文件的函数,专门下载函数
    #downlowd_image(img_url1,"1.gif")


    #批量进行join()，需要一个参数协程的列表
    gevent.joinall([
            gevent.spawn(downlowd_image,img_url1,"1.gif"),
            gevent.spawn(downlowd_image,img_url2,"2.gif"),
            gevent.spawn(downlowd_image,img_url3,"3.gif")
    ])





if __name__ == "__main__":
    main()