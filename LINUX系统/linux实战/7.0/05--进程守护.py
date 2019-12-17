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
def work1():
    for i in range(10):
        print("这个在运行work1.....")
        time.sleep(0.5)


if __name__ == "__main__":
    process_obj = multiprocessing.Process(target=work1)
    #线程   setDaemon(True)
    #3进程守护      proxess_obj.daemon=True
    #process_obj.daemon = True 
    process_obj.start()


    time.sleep(2)
    print("我要死")
    #终止子线程执行    不是守护  就是死之前  杀死他
    process_obj.terminate()
    exit()
    print("XXXXXXXXXXXXXXX")