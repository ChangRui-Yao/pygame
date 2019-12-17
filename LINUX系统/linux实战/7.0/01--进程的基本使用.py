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
    process_obj.start()
    print("XXXXXXXX")