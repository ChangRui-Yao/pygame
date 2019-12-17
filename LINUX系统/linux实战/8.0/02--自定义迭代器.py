"""
#1MyList()类
    初始化方法__init__()
    对外提供迭代器__iter__()
    添加数据addIter()
2MyListIterator()
    初始化方法__init__()
    迭代器方法__iter__()
    获得下一个元素值__next__()

目标：
mylist = Mylist()
for value in mylist:
    print(value)


"""



#Mylist类
class MyList(object):
    #构造方法
    def __init__(self):
        self.items = []


            #迭代器方法
    def __iter__(self):
        #创建一个自定义迭代器的对象
        my_listitrtator = MyListIterator(self.items)
        #迭代器对象
        return my_listitrtator

        #添加函数方法
    def addItem(self,data):
        #保存数据
        self.items.append(data)
        print(self.items)

class MyListIterator(object):
    def __init__(self,items):
        
        #定义实力属性保存传递进来的items
        self.items = items
        
        #定义变量记录迭代器迭代的位置
        self.weizhi = 0
    
    def __iter__(self):
        pass
    
    #获取下一个元素的方法
    #next(my_listitrtator)的时候就会调用__next__()方法
    
    
    def __next__(self):
        #判断当前的下表是否越界
        if self.weizhi < len(self.items):

            #如果没越界 根据下标 获取元素值   下标加1   返回下表对应的数据
            data = self.items[self.weizhi]
            #下表位置加一
            self.weizhi += 1
            #返回下标对应的值
            return data
            # 如果越界 ,直接抛出异常        
        else:
            #raise用于主动抛出错误
            #StopIteration 停止迭代
            raise StopIteration 

if __name__ == "__main__":
    mylist = MyList()
    mylist.addItem("上官婉儿")
    mylist.addItem("韩信")
    mylist.addItem("伽罗")

    #for循环本质：1iter(mylist)获得mylist的迭代器   -->>调用__iter__
                #2next(迭代器) 获取下一个值
                #3捕获异常
    #for value in mylist:
    #    print("name:",value)
    
    
    mylist_iterator = iter(mylist)
    file_data = next(mylist_iterator)
    print(file_data)