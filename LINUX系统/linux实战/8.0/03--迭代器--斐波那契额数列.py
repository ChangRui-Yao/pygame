"""







"""
class Fibnacci(object):
    def __init__(self,num):
        self.num = num
        self.weizhi = 0
        #保存斐波那契额数列的第一列和第二列
        self.a = 1
        self.b = 1
    
    
    #__iter__()
    def __iter__(self):

        #返回自己
        return self

    def __next__(self):
        #判断下标是否超过要生成的范围
        if self.weizhi <self.num:
                
            #定义变量保存A的值
            data = self.a
            #a=b  b = a+d
            self.a,self.b = self.b, self.a + self.b
            #当前列数加1
            self.weizhi += 1
            #返回a的值
            return data
        else:
            #主动抛出异常
            raise StopIteration
if __name__ == "__main__":
    l1 = Fibnacci(5)
    #value = next(l1)
    #print(value)
    #迭代器本身又是一个迭代器
    for i in l1:
        print(i)