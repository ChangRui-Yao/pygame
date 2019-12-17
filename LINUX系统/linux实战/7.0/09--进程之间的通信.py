"""
#1准备两个进程
#2准备一个队列
#3一个进程负责向进程中put数据，然后把队列传递到另一个进程
#4另一个队列进行读取

"""
import time
import multiprocessing
#写入数据到队列的函数
def write_queue(queue):
    #for循环写入数据
    for i in range(1000):
        if queue.full():
            print("队列已满")
            time.sleep(0.5)
            continue
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
            time.sleep(0.5)
            continue
        #从队列中读取数据
        value = queue.get()
        print("已经读取，读取到:",value)


if __name__ == "__main__":

#创建一个空的队列
    queue = multiprocessing.Queue(5)
#创建两个进程，分别写数据。读数据
    write1_queue = multiprocessing.Process(target=write_queue,args=(queue, ))
    read1_queue = multiprocessing.Process(target=read_queue,args=(queue, ))
    #write1_queue.daemon = True
    #read1_queue.daemon = True 
    write1_queue.start()
    #优先让写进程执行，结束后再执行读数据  join()   优先写 在去读
        #swrite1_queue.join()

    read1_queue.start()
    #while True:
    #print("123")
    time.sleep(10)
    write1_queue.terminate()
    read1_queue.terminate()