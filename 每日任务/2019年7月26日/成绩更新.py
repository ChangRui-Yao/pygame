import os
# -*- coding: utf_8 -*-
def getfileDatas(filepath,zidian_1):
    try:
        i = open(filepath,'r',encoding='utf-8')#打开文件对象
        stri = i.read()#读取文件
        i.close()#关闭文件
        listfiles = stri.split('\n')#切片
        for onefilese in listfiles:#循环
            listonfile = onefilese.split(',')#切片格式
            if len(listonfile) == 2:#判断listonfile里数据数量
                zidian_1[listonfile[0]] = listonfile[1]
    finally:
        if i:
            i.close()
def chaxunchengji(zidian_1):
    str = input("请输入查询对象:")
    d = zidian_1.get(str,-1)
    if d == -1:
        print("学生",str,"不存在")
        return
    print("学生: ",str,"成绩为: ",zidian_1[str])
    
dictdata = {}
getfileDatas('./成绩.txt',zidian_1)
chaxunchengji(zidian_1)
