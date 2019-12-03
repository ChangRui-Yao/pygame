import os
import time
def MainFun():
    
    
#---在此处获得了这个文件夹内所有的名字
    list_1 = os.listdir('G:\\PersonPro\\PythonPro\\每日任务\\2019年11月10日\\log')
    test = input("请输入用户名：")
#print(list_1)
    if test in list_1:
        
        while(1):
            
            
            username = test + ":"
            userstr = input(username)
            if username == "ok":
                return
        #-------在这里得到添加文件的路径
            filepath = "G:\\PersonPro\\PythonPro\\每日任务\\2019年11月10日\\log\\" +test + "\\" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
              

        else:
            print("此人名不存在是否创建:[Yes/No]")
            str = input()
            if str == "Yes":
                f = open("G:\\PersonPro\\PythonPro\\每日任务\\2019年11月10日\\log",mode = 'a')
                strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                strtime +=" "+ str + "\n"
                f.write(strtime)
                f.close()
            else:
                return
MainFun()





















#while(1):
#        #-------在这里得到添加文件的路径以及名字
#    filepath = "G:\\PersonPro\\PythonPro\\每日任务\\2019年11月10日\\log\\" +test + "\\" + time.strftime('%Y-%m-%d',time.localtime(time.time()))
#    username = test + ":"
#    userstr = input(username)
#    if username == "ok":
#        return
