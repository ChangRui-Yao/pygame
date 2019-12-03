import os
# -*- coding: utf-8 -*-
def getfileDatas(filepath,dictdata):
    try:
        file = open(filepath,'r',encoding='utf-8')
        strfile = file.read()
        file.close()
        listfiles = strfile.split('\n')
        for onefiles in listfiles:
            listonfile = onefiles.split(',')
            if len(listonfile) == 2:
                dictdata[listonfile[0]] = listonfile[1]
    finally:
        if file:
            file.close()
def findStudentCount(dictdata):
    str = input("请输入学生名称:")
    d = dictdata.get(str,-1)
    if d == -1:
        print("学生: ",str,"不存在")
        return
    print("学生: ",str," 成绩为: ",dictdata[str])
    
dictdata = {}
getfileDatas("./成绩.txt",dictdata)
findStudentCount(dictdata)
