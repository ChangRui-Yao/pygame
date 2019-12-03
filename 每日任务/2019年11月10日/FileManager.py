import os
import time

def checkDir(path):
    if os.path.exists(path):
        return True
    else:
        print("此人名不存在是否创建:[Yes/No]")
        str = input()
        if str == "Yes":
            os.makedirs(path)
            if os.path.exists(path):
                return True
    return False
        

def getDirName(path):
    listfiles = os.listdir(path)
    listdir = []
    for dir in listfiles:
        if os.path.isdir(path):
            listdir.append(dir)
    return listdir

def WriteToFile(path,str):
    #首先判断文件是否存在
    f = open(path,mode='a')
    strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    strtime +=" "+ str + "\n"
    f.write(strtime)
    f.close()
