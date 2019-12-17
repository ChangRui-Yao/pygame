"""

#greenlet实现协程的步骤
    #1导入模块
    #2创建两个生成器   work1   work2
    #3创建green对象
    #4手动switch切换任务

"""
import time
from greenlet import greenlet
def work1():
    while True:
        print("正在执行work1.....")
        time.sleep(0.5)
        #切换到第二个任务中
        g2.switch()

def work2():
    while True:
        print("正在执行work2.......................")
        time.sleep(0.5)
        #切换work1
        g1.switch()

if __name__ == "__main__":
    #创建green对象
    #greenlet(函数名)
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    #执行work1
    g1.switch()
    #g2.switch()