import time
import threading
"""
#唱歌的函数
#跳舞的函数
调用

"""

def sing():
    for i in range(5):
        print("正在唱歌...",threading.current_thread())
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("正在跳舞.................",threading.current_thread())
        time.sleep(0.5)

#-调用
if __name__ == "__main__":
    thread_list = threading.enumerate()
    print(thread_list)
    #---获得正在活跃的线程列表
    thread_list = threading.enumerate()
    print("当前线程数量：",len(thread_list))


    #-获得线程名称
    print(threading.current_thread())

    thread_sing = threading.Thread(target=sing)
    thread_dange = threading.Thread(target=dance)
    
    #thread_list = threading.enumerate()
    #print("2当前线程数量",len(thread_list))

    thread_sing.start()
    thread_dange.start()
