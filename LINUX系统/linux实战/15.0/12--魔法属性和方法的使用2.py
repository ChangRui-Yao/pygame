class Goods(object):
    """这是一个商品的类"""
    #类属性
    goods_color = "白色"
    def __init__(self):
        #实例属性
        self.orgg_price = 100
        self.discount = 0.7

    def set_price(self):
        """这是Goods类中设置价格的方法"""
        pass


    def __call__(self,*args,**kwargs):
        print("__call__方法正在被调用")


    def __str__(self):
        return "我是一个寂寞的对象"


    def __del__(self):
        print("__del__正在执行")

    
    def __getitem__(self,item):
        print("key = ",item)

    
    def __setitem__(self,key,item):
        print("key = %s,item = %s" % (key,item))

    def __delitem__(self,key):
        print("要删除key = ",key)


goods = Goods()
#当对象名加()  就会去调用对象的__call__()方法
#goods()
#print  打印对象
#print(goods)


#通过__dict__获取对象信息  对象.__dict__ ，返回字典
#print(goods.__dict__)
#获取累的信息，  类名.__dict__   ,返回字典
#print(Goods.__dict__)



#dict1 = {}
#dict1["a"] = 10

#goods["a"]  调用__geiitem__方法
#goods["a"]

#goods["a"] = 10 调用__setitem__方法
#goods["a"] = 10

#del goods["a"]
del goods["a"]