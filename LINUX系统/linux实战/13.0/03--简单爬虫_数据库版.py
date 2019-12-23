"""
#一，定义函数获取列表页的影片信息获取内容页的地址get_movie_links()
#1定义列表页地址https://www.ygdy8.net/html/gndy/dyzz/index.html
#2打开列表页，获取数据
#3解码获取到的数据
#4使用正则得到所有影片内容页的地址
#二，定义主函数main()


#定义专门的函数，负责保存数据         add_film()
            #1定义SQL  准备差如数据
            #2执行insert
            #3commit
#定义专门的函数，检测数据库是否存在相同的函数   film_exist()
            #1根据影片名称和地址进行查询    
            #2执行查询并获取查询的记录数
            #3如果获取到的记录数>0      return  true
            #4如果获取到的记录数 =0      return  false
#创建一个全局连接对象
#创建一个全局游标对象
#关闭游标对象
关闭连接
"""


import re
import urllib.request
import pymysql

def add_film(file_name,file_link):
    """保存影片到数据库"""
    #定义SQL  准备差如数据
    sql = "insert into movie_link values (null,%s,%s)"
    #执行insert
    ret = cur.execute(sql,[file_name,file_link])
    #如果插入成功给条提示
    if ret:
        print("保存成功，[%s]" % file_name)


def film_exist(file_name,file_link):
    """用于检测数据是否存在"""
    #1根据影片名称和地址进行查询
    sql = "select id from movie_link where file_name=%s and file_link=%s limit 1"
    #2执行查询并获取查询的记录数
    ret = cur.execute(sql,[file_name,file_link])
    #3如果获取到的记录数>0      return  true
    if ret:
        return True
    #4如果获取到的记录数 =0      return  false
    else:
        return False

def get_movie_links():
    movie_url = "https://www.dytt8.net"
    #定义字典保存影片信息
    films_dict = {}
    
    
    #获取列表页信息
    #1定义列表页地址https://www.ygdy8.net/html/gndy/dyzz/index.html
    film_list_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
    #2打开列表页，获取数据
    response_list = urllib.request.urlopen(film_list_url)
        #2.1通过read读取网络资源 
    response_data = response_list.read()
    #if response_data:
            #3解码获取到的数据
    response_list_text = response_data.decode("gbk","ignore")   
    #4使用正则得到所有影片内容页的地址
    #print(response_list_text)
    #根据正则findall查找所有影片对应的内容地址
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>",response_list_text)
    #print(url_list)
    i = 1
    #循环遍历拼接所有影片页的详细地址
    for content_url,movie_name in url_list:
        #拼接内容页地址
        content_url = movie_url + content_url
        #print("影片名称",movie_name,"内容页地址：",content_url)
        #打开内容页地址获取数据
        response_content = urllib.request.urlopen(content_url)
        #读取
        response_content_data = response_content.read()
        #解码得到内容页的文本内容
        response_content_text = response_content_data.decode("gbk","ignore")
        #正则得到下载的链接地址
        result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*?)\">",response_content_text)
        #print(result.group(1))

        #组建一个字典   {"名称":"地址",}
        films_dict[movie_name] = result.group(1)
        print("已经获取到[%d]条信息" % i)
        i += 1
    return films_dict



def main():
    movie_dict = get_movie_links()
    #print(movie_dict)

    #把字典遍历输出
    for movie_name,movie_links in movie_dict.items():
        print("%s  |  %s" % (movie_name,movie_links))
        #判断如果数据库存在相同数据  不再插入
        if film_exist(movie_name,movie_links):
            print("保存失败,影片已存在：[%s]" % movie_name)
            continue
        #调用add_movie()方法项数据库添加参数
        add_film(movie_name,movie_links)

if __name__ == "__main__":
    #创建一个全局连接对象
    conn = pymysql.connect(host="192.168.43.153",user="jiangfeng",password="123456",database="movie_db")
    #创建一个全局游标对象
    cur = conn.cursor()
    
    main()
    conn.commit()
    #关闭游标对象
    cur.close()
    conn.close()

