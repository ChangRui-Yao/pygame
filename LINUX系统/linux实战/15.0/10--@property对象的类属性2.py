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
    def get_price(self):
        return self.org_price * self.dicount


    #设置价格方法
    def set_price(self,val):
        if val > 0:
            self.org_price = val


    #删除价格方法
    def del_price(self):
        print("执行了deleter方法")

    #property （第一个参数，第二个参数，第三个参数，第四个参数）
    #第一个参数，当我们foo.BAR，自动调用第一个参数的方法
    #第二个参数，当我们foo.BAR = 100,会自动调用第二个参数的方法
    #第三个参数，当我们del.foo.BAR,会自动调用第三个参数的方法
    #第四个参数，当我们Foo.BAR.__doc__,会自动获取第四个参数的内容   
    BAR =property(get_price,set_price,del_price,"BAR是一个property对象")

if __name__ == "__main__":
    #创建对象
    goods = Goods()
            #相当于调用goods.get_price()
    print(goods.BAR)
    #设置价格
    goods.BAR = 500
            #相当于调用goods.set_price(500)
    print(goods.BAR)
    #删除价格
            #相当于调用 del goods.BAR    ========   @del_price.deleter
    del goods.BAR
    #获取对象描述
            #相当于获取类的描述信息
    print(Goods.BAR.__doc__)