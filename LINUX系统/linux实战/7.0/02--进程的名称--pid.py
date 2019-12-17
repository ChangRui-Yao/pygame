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
import os
def work1():
    for i in range(10):
        #获得当前进程的名称
        #print("这个在运行work1.....",multiprocessing.current_process())
        
        #获取进程的编号
        #方式一
        #print("这个在运行work1.....",multiprocessing.current_process().pid)
        #方式二
        #print("work1",os.getpid())
        
        #获取进程的父id ppid -->parent process id
        #print("work1",os.getppid())
        
        print("work1名字：",multiprocessing.current_process(),"work1编号：",os.getpid())
        time.sleep(2)
        
        #kill-9杀掉进程   kill-15等他执行完干掉
        #kill-9()


if __name__ == "__main__":
    #获取主进程的名称
    #multiprocessing.current_process()获取当前进程名称
    print(multiprocessing.current_process())
    #获取进程的编号  process id -->> pid
    #方式一multiprocessing.current_process().pid
    #print("主进程编号",multiprocessing.current_process().pid)
    #方式二使用os模块来获取
    print("主进程编号",os.getpid())
    
    
    
    
    #1导入模块
    #2通过模块提供的process创建进程对象
    #3进程对象启动
    #                           target指定子进程要执行的分支函数
    #                           name指定子进程名称
    process_obj = multiprocessing.Process(target=work1,name="P1")
    process_obj.start()
    print("XXXXXXXX")