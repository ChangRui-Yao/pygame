class Foo(object):
    def __init__(self, num):
        self.num = num

    @property        #用这个装饰器装饰这个方法
    def prop(self):
        return self.num



foo = Foo(100)
#print(foo.prop())


#           foo.prop     ------------>>      foo.prop()
#               像使用属性一样去使用方法，获取值
print(foo.prop)