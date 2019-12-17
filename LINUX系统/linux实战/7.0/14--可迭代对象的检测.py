from collections import Iterable



ret = isinstance([1,2,3,4],Iterable)
print(ret)
print("--" * 20)


ret = isinstance(100,Iterable)
print(ret)
print("--" * 20)

#自定义类
class Myclass(object):
    #增加一个__iter__方法
    #该方法就是一个迭代器
    def __iter__(self):
        pass
#创建对象
myclass = Myclass()

ret = isinstance(myclass,Iterable)
print(ret)
print("--" * 20)


#可遍历对象就是可迭代对象
#列表元祖字典字符串 都是可迭代对象    
#数值100和自定义Myclass都是不可迭代的
#Myclass对象所属的类MyClass，如果包含了__iter__()，此时myclasss就是一个可迭代对象

#可迭代对象的本质：对象所属的类中包含了__iter__()  方法
#3检测一个对象是否可以迭代，用isinstance()  函数检测