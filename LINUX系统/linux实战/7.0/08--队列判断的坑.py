import multiprocessing
import time


queue = multiprocessing.Queue(3)

queue.put(1)
queue.put(1)
queue.put(1)


#判断队列是否为空
isEmpty = queue.empty()

print("isEmpty=>",isEmpty)


###############################3333333333这个坑  没遇到2333333333333333333
