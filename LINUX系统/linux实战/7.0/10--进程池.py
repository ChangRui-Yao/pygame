"""
#1创建一个函数 模拟文件拷贝
#2创建一个进程池    长度为3    （表示进程池中最多能够创建3个进程）
#3先用进程池同步方式拷贝文件
#4再用进程池异步方式拷贝文件
"""
import time
import multiprocessing

#1创建一个函数 模拟文件拷贝
def copy_work():
    print("正在拷贝文件.....",multiprocessing.current_process())
    time.sleep(0.5)

if __name__ == "__main__":
#2创建一个进程池    长度为3    （表示进程池中最多能够创建3个进程）
    #进程池创建两部
    #导入模块
    #创建进程池pool = multiprocessing.pool(2)     最大允许创建两个进程
    pool = multiprocessing.Pool(3)
    for i in range(10):
        #    copy_work()
        #3先用进程池同步方式拷贝文件   #pool.apply(函数名，(传递给函数的参数1，参数2))
        #pool.apply(copy_work)
        #4再用进程池异步方式拷贝文件
                #如果使用apply_async方式，需要做两点
                #1)pool.close()             表示不在接受新的任务
                #2）主进程不在等待进程池执行结束后再退出，需要进程池join()
                        #pool.join()    让主进程等待进程池执行结束后 在退出
        pool.apply_async(copy_work)
    #1)pool.close()             表示不在接受新的任务
    pool.close()
    #2）主进程不在等待进程池执行结束后再退出，需要进程池join()
                        #pool.join()    让主进程等待进程池执行结束后 在退出
    pool.join()