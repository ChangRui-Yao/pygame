"""
#1一个可迭代对象可以提供一个迭代器
#2可迭代对象 ----》iter(刻碟代对象)------》next(迭代器)
                    迭代器                  下一个元素


#迭代器特点：记住我们遍历的位置，
#           提供下一个元素的值           

for循环的本质：
1) 通过 iter(可迭代对象)   获得要遍历对象的迭代器
2）next(迭代器)获取下一个元素
3）帮我们捕获了   StopIteration  异常   

"""
data_list = [1,3,5,7,9]
#是一个可迭代对象
#for value in data_list:
#    print(value)
l1_iterator = iter(data_list)
next_data = next(l1_iterator)
print(next_data)


next_data = next(l1_iterator)
print(next_data)



next_data = next(l1_iterator)
print(next_data)


#自定义迭代器类
#1)，必须含有__iter__()方法
#2）,必须含有__next__（）方法
class MyIterator(object):
    def __iter__(self):
        pass
            #当next(迭代器时)，会自动调用该方法
    def __next__(self):
        pass