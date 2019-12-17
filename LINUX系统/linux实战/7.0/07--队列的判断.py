"""
#1判断是否已经满
#2判断是否已空

#3取出队列队列中消息的个数

"""
import multiprocessing
#创建一个疮毒为3的对列
queue = multiprocessing.Queue(3)

queue.put(1)
queue.put(2)
#queue.put(3)
print(queue._maxsize)
buffer = queue._recv_bytes()
print(type(buffer))

#tes=buffer.decode()
tes = bytes.decode(buffer)
#取值
value = queue.get()
#value = queue.get()
#value = queue.get()

#1判断是否已经满
#queue.full()   判断队列是否以及满了  True  满  False   未满
isFull = queue.full()
print("isfull--------->",isFull)

#3取出队列队列中消息的个数
##quese.qsize    当前消息的个数
print("当前消息的个数：",queue.qsize())

##2判断是否已空
##queue.empty   判断队列是否为空   为空True     不为空 False
is_Empty = queue.empty()
print("is_empty----------->",is_Empty)