#--------monlocal---------
def fun3():
        x = 5
        def fun4():
            #--------强制说明x不是一个局部变量-------
                nonlocal  x
                #-------x = x的平方
                x *= x
                return x
        return fun4()
fun3()
