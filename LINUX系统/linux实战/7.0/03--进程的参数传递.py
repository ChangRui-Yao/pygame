"""
#1导入模块
#2通过模块提供的process创建进程对象
#3进程对象启动
"""
#1导入模块
#2通过模块提供的process创建进程对象
#3进程对象启动
import time
import multiprocessing
def work1(a,b,c):
    print("参数",a,b,c)
    for i in range(10):
        print("这个在运行work1.....")
        time.sleep(0.5)


if __name__ == "__main__":

    #参数传递由三种方式
        #1使用 args  传递元组
        #2使用 kwargs  传递字典
        #3混合使用  args  和 kwargs




    process_obj = multiprocessing.Process(target=work1,args=(10,100,1000))
    process_obj.start()
    print("XXXXXXXX")