import multiprocessing
import time
g_num = 10

#1work1  对全局变量进行累加
def work1():
    global g_num
    for i in range(10):
        g_num += 1

    print("------work1------",g_num)
#2work2  读取全局变量     
def work2():
    print("-----work2-----",g_num)



if __name__ == "__main__":
    #创建进程
    l1 = multiprocessing.Process(target=work1)
    l2 = multiprocessing.Process(target=work2)

    l1.start()
    l2.start()

    time.sleep(3)
    
    print("main",g_num)