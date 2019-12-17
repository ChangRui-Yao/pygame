import time
import threading
"""
#唱歌的函数
#跳舞的函数
调用

"""

def sing(a,b,c):
    #打印参数
    print("参数", a, b, c)
    for i in range(5):
        print("正在唱歌...")
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("正在跳舞.................")
        time.sleep(0.5)

#-调用
if __name__ == "__main__":
    #在线程中传递参数三种方法
    #1使用元组传递threading.Thread(target=XXX,args=[参数1，参数2，参数3....])
    #thread_sing = threading.Thread(target=sing,args=(10,100,1000))
    #2使用字典传递
    #thread_sing = threading.Thread(target=XXX,kwargs={"参数名:参数值,"参数名":参数值.......})
    #thread_sing = threading.Thread(target=sing,kwargs={"a": 10,"c": 1000,"b": 100})
    #3混合使用元组和字典
    #thread_sing = threading.Thread(target=sing,args=[参数1，参数2，参数3....]，kwargs={"参数名:参数值,"参数名":参数值.......})
    thread_sing = threading.Thread(target=sing,args=(10, ),kwargs={"c":1000,"b":100})
    thread_dange = threading.Thread(target=dance)
    thread_sing.start()
    thread_dange.start()