"""
#1创建一把锁
#2在使用资源之前锁定资源
#3使用资源后解锁资源


"""
import threading
import time
    #观察work1线程对全局变量的修改，在work2中能否查看修改后的结果
#定义全局变量
g_num = 0
#work1
def work1():
    #声明g_num是一个全局变量
    global g_num
        #进行上锁
    lock_1.acquire()
    for i in range(1000000):
        g_num += 1
    lock_1.release()    
    print("work1........数值",g_num,"........")
#work2
def work2():
    #声明g_num是一个全局变量
    global g_num
    lock_1.acquire()
    for i in range(1000000):
        g_num += 1
    lock_1.release()
    
    print("work2........数值",g_num,"........")
#创建两个子线程
if __name__ == "__main__":
    #1创建一把互斥锁
    lock_1 = threading.Lock()


    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    #启动线程
    t1.start()
    #优先执行t1，t1执行完毕，t2才能执行
    #t1.join()
    t2.start()

    #print(len(threading.enumerate()))
    while len(threading.enumerate()) !=9:
        time.sleep(1)
    #在t1和t2执行完毕后打印g_num
    print("main---------------数值",g_num,".....")

