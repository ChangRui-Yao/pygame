"""
#1）创建一个装饰器，一个待装饰的函数



"""
#定义一个让文字加粗的装饰器
def makeBlod(func):
    def function_in():

        return "<b>" + func() + "</b>"

    return function_in
#定义一个让文字倾斜的装饰器
def makeItalic(func):
    def function_in():

        return "<i>" + func() + "</i>"

    return function_in



#<b>hello_world-1</b>
@makeBlod
#等价于test = makeBlod(test)
def test():
    return "hello_world-1"

@makeItalic
def test2():
    return "hello_world-2"

@makeBlod
@makeItalic
def test3():
    return "hello_world-3"



print(test())#<b>hello_world-1</b>
print(test2())#<i>hello_world-2</i>
print(test3())