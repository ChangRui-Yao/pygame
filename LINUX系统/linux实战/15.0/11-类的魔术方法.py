class Goods(object):
    """这是一个商品的类"""

    def set_price(self):
        """这是Goods类中设置价格的方法"""
        pass
    def __del__(self):
        print("__del__正在执行")

#1类的描述信息
print(Goods.__doc__)

#2对象方法的描述
#对象名.方法名
goods = Goods()
print(goods.set_price.__doc__)


#3获取当前模块
print(goods.__module__)
#4获取对象所属的类
print(goods.__class__)


#5删除对象会执行  对象的__del__方法
del goods