"""
#首先先需要两个类  一个用来创造列表  一个迭代器类
#class MyList():
#构造方法
# __init__():
#迭代器方法
#__iter__():
#添加函数的方法
#additem():


#class MyItemarto():
#构造函数
#__init__():
#迭代器
#__iter__():
#下一个参数
#next():

"""
class MyList(object):
    #构造方法
    def __init__(self):
        self.items = []
    #迭代器方法
    def __iter__(self):
        myitemarto = MyItemarto(self.items)
        return myitemarto
    #添加函数的方法
    def additem(self,items):
        self.items.append(items)
        print(self.items)

class MyItemarto(object):
    #构造函数
    def __init__(self,items):
        self.items = items
        self.weizhi = 0
    #迭代器
    def __iter__(self):
        pass

    #下一个参数
    def __next__(self):
        if self.weizhi < len(self.items):
            data = self.items[self.weizhi]
            self.weizhi += 1
            return data
        else:
            raise StopIteration        
        




if __name__ == "__main__":
    mylist = MyList()

    mylist.additem("张飞")
    mylist.additem("关羽")
    mylist.additem("13131")
    
    for i in mylist:
        print(i)