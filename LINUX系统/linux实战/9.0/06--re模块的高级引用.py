"""
#1导入模块
#2t通过match   方法，验证正则
#3加个判断  是否匹配成功
#4如果成功获取匹配的结果
"""
import re
#2t通过match   方法，验证正则
    #re.match(正则表达式，要验证的字符串)
    #match()方法如果匹配成功，返回match_object对象
    #如果失败  返回None
#result = re.match("\w{4,20}@163\.com$","11hello@163.com")
#result = re.search("hello","11hello@163.com")
#match和search的区别
        #使用math方法，正则表达式从需要检测开头进行匹配，成功返回matchobject对象，如果失败返回None
        #sechch在需要检测字符串以搜索的方法进行匹配，全文进行匹配，有则返回matchobject对象，如果失败返回None
#一，search的使用
#result = re.search("\d+","阅读次数：9999")
#二，findall()   搜索全部，返回值是一个列表
#result = re.findall("\d+","阅读次数：9999,转发次数：6666，评论次数：8888")
#三sub用法  查找要替换的字符串，并且替换为指定的内容，返回值是替换后的字符串
#result = re.sub("\d+","10000","阅读次数：9999,转发次数：6666，评论次数：8888")
#四按照正则表达式拆分字符串，返回值是一个列表！！
result = re.split("\d+,*","阅读次数：9999,转发次数：6666，评论次数：8888")
#3加个判断  是否匹配成功
if result:
    print("匹配成功")
    print("匹配结果:",result)
else:
    print("匹配失败")
#4如果成功获取匹配的结果