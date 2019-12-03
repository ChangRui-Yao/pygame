##for i in "jiangfeng":
##    print(i)

lists = {"姜枫":"123456",\
         "婉儿":"惊鸿之笔",\
         "亚瑟":"哈哈哈哈"}
for i in lists:
    #---------注意这里调用字典lists里i  对应的值 使用的是[]
    print("%s -> %s" % (i,lists[i]))
    

#-----------迭代操作使用了两个关键的BIF
        #--iter()
string = "jiangfeng"
t = iter(string)           




        #--next()  使用这个next()
next(t)

#---------------------------在这用while循环诠释了for语句的用法
i = next(t)

for i in t:
    print(i)


while True:
    try:
        i = next(t)
        #-----在这里如果捕获这个异常 则break出去
    except StopIteration:
        break
    print(i)

#----------关于迭代器的魔法方法有两个
    #--------iter()    ===    __iter__()
    
    
    #--------next()    ===    __next__()
#-------------------------------------------------斐波那契数迭代实现
class Fibs:
    def __init__(self,n=10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b ,self.a + self.b
        if self.a > self.n:
            #-----注意在这里引发了这个异常
            raise StopIteration
        return self.a
fibs = Fibs(100)
for each in fibs:
##    if each <20:
       print(each)
##    else:
##        break
