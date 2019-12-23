class Foo(object):
    def get_bar(self):
        return "laotie"
        #property 类属性
        #property （第一个参数，第二个参数，第三个参数，第四个参数）
        #第一个参数，当我们foo.BAR，自动调用第一个参数的方法
        #第二个参数，当我们foo.BAR = 100,会自动调用第二个参数的方法
        #第三个参数，当我们del.foo.BAR,会自动调用第三个参数的方法
        #第四个参数，当我们Foo.BAR.__doc__,会自动获取第四个参数的内容
    BAR = property(get_bar)

foo = Foo()
#print(foo.get_bar)
print(foo.BAR)