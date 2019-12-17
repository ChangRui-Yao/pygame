"""
#1定义函数
#2调用

#子线程创建的步骤
    #1导入模块 threding
    #2只用threding.Tread() 创建对象（子线程对象）
    #指定子线程执行的分支
    #启动子线程   线程对象.start()
"""
import time
import threading

def saysorry():
    print("对不起我错了")
    time.sleep(0.5)

if __name__ in "__main__":


    for i in range(5):

        #2使用threding.Tread() 创建对象（子线程对象）
        #指定子线程执行的分支
            #参数 target=函数名     threading.Thread(target=函数名)
        thread_obj = threading.Thread(target=saysorry)

        #启动子线程   线程对象.start()
        #线程只有 调用了.start()才会执行
        thread_obj.start()
    print("XXXX")