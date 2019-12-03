import FileManager as fman
import time
def MainFun():
    userlist = fman.getDirName("./log")
    str = input("请输入您的用户名:")
    if str not in userlist:
        dirstr = "./log/"+str
        if fman.checkDir(dirstr) == False:
            return
        
    while(1):
        filepath = "./log/"+str+ "/" + time.strftime('%Y年-%m月-%d日',time.localtime(time.time())) + ".txt"
        print(filepath)
        username = str + ": "
        userstr = input(username)
        if userstr == "ok":
            return
        fman.WriteToFile(filepath,userstr)
        
        
MainFun()
