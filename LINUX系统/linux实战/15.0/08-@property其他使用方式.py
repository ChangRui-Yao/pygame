"""
#类goods
#初始化方法
#获取价格方法
#设置价格方法
#删除价格方法


"""
#类goods
class Goods(object):
    #初始化方法
    def __init__(self):
        #初始化原价
        self.org_price = 1000
        #初始化折扣
        self.dicount = 0.7
    #获取价格方法
    @property
    def price(self):
        return self.org_price * self.dicount
    #设置价格方法
    @price.setter
    def price(self,val):
        if val > 0:
            self.org_price = val
    #删除价格方法
    @price.deleter
    def price(self):
        print("执行了deleter方法")


goods = Goods()
#goods.proce = goods.price()
#获取当前价格
print(goods.price)

#加入装饰器后
#设置原价     goods.price = 500 等价于 good.price(500)
goods.price = 500
print(goods.price)


#del goods.price 等价于 goods.deleter  装饰的方法
del goods.price