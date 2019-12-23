"""
#存在函数嵌套关系
#内部函数引用了外部函数的变量
#外部函数返回内部函数的地址

"""
def function_out(num):

    def function_in():
        #造成错误的原因  ：编译器认为内城函数已经定义了num变量，优先使用内层的
        #如果在内层定义了和外层同名的变量，而且需要使用外层的变量
        #nonlocal  表示不使用内层函数变量  而是使用外层函数的变量
        nonlocal num

        print("这是内部函数num", num)
        #内部函数内部定义的变量
        print(num)
        num = 88
        print(num)
    return function_in
#调用外层函数
ret = function_out(10)
ret()