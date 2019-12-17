"""
#gevent    好处：能够自动识别程序中需要耗时的地方，自动切换到
#genvent实现协程的步骤   
    #1导入模块
    #4指派任务

"""
#一般放到开头处
from gevent import monkey
monkey.patch_all()

import time
import gevent
def work1():
    while True:
                                #------gevent.getcurrent()查看执行当前任务的协程
        print("正在执行work1.....",gevent.getcurrent())
        time.sleep(0.5)
        #默认情况下time.sleep()不能被gevent识别为耗时操作
                #1把time.sleep()换成gevent.sleep()
                #2给gevent  打补丁  （目的，让gevent,识别  time.sleep()）
                    #打补丁，在不修改程序源代码的情况下  为程序增加新的功能
                #如何打补丁
                    #1)导入模块  import monkey 模块（猴子补丁）from gevent import monkey
                    #2)进行破解  monkey.patch_all()
        #gevent.sleep(0.5)


def work2():
    while True:
        print("正在执行work2.......................",gevent.getcurrent())
        time.sleep(0.5)
        #gevent.sleep(0.5)

if __name__ == "__main__":
    #指派任务
    #gevent.spawn(函数名，参数1，参数为，......)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)


    #本就是协程，让主线程等待协程执行完毕再退出
    g1.join()
    g2.join()