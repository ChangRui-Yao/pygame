import threading
import time
    #观察work1线程对全局变量的修改，在work2中能否查看修改后的结果
#定义全局变量
g_num = 0
#work1
def work1():
    #声明g_num是一个全局变量
    global g_num

    for i in range(10):
        g_num += 1
    
    print("work1........",g_num)

#work2
def work2():
    print("work2---------",g_num)

#创建两个子线程
if __name__ == "__main__":
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    
    #启动线程
    t1.start()
    t2.start()

    while len(threading.enumerate()) !=1:
        time.sleep(1)
    #在t1和t2执行完毕后打印g_num
    print("main---------------",g_num)
