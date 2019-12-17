import time
import multiprocessing
#写入数据到队列的函数
def write_queue(queue):
    #for循环写入数据
    for i in range(10):
        if queue.full():
            print("队列已满")
            break
        #想队列中写入值
        queue.put(i)
        print("写入成功，已经写入:",i)
        time.sleep(0.5)
#读取数列并显示的函数
def read_queue(queue):
    while True:
        #判断队列是否为空
        if queue.qsize() == 0:
            print("队列已空")
            break
        #从队列中读取数据
        value = queue.get()
        print("已经读取，读取到:",value)


if __name__ == "__main__":

    #创建一个进程池
    pool = multiprocessing.Pool(2)

    #创建进程池中的队列
    queue = multiprocessing.Manager().Queue(5)

    #3使用进程池执行任务
    #1同步执行
    #pool.apply(write_queue,(queue, ))
    #pool.apply(read_queue,(queue, ))

    #异步执行
    result = pool.apply_async(write_queue,(queue, ))
    result.wait()
    pool.apply_async(read_queue,(queue, ))

    #pool.close()表示不再接受新的任务
    #pool.join()表示主进程会等待进程池执行结束后再退出
    pool.close()
    pool.join()