"""
#生成器是一个特殊的迭代器（）保存位置，返回下一个值

next

#生成器创建方式
#1）列表推导式
#2）函数中使用了 yield

"""
#列表推导式
data_list1 = [x*2 for x in range(10)]
for value in data_list1:
    print(value,end=" ")


#生成器的创建一
data_list2 = (x*2 for x in range(10))
print(data_list2)
#通过next获取下一个值
value = next(data_list2)
print("------->",value)

print("************************************************")

def text():
    return 10
m = text()
print("m=",m)

print("*********************************************")
#使用yield创建了一个生成器      
def text2():
    yield 10
n = text2()
yulue = next(n)
print("n------->",yulue)