"""
#1自定义线程类继承threading.Thread类
#2重写父类（threading_Thread）的run方法
#3创建子类对象  子类对象.start
threading.Thread():
    def start():
        self.run()
    def run():
        pass


"""



import threading
import time

#自定义线程类
class MyThread(threading.Thread):
    def __init__(self,num):
        #当我们重写父类的__init__方法，需要先调用父类的__init__方法
        super().__init__()
        self.num = num

    #重写父类的run方法
    def run(self):
        for i in range(5):
            #self.name也是从父类继承的属性
            print("正在执行子线程的run方法",i,self.name,self.num)
            time.sleep(0.5)

if __name__ == "__main__":
    #创建对象
    mythread = MyThread(10)
    #线程对象.start()  启动线程
    #子类从父类继承的start()方法
    mythread.start()
    print("XXXXXXX")