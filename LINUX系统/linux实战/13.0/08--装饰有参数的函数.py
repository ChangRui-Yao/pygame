def function_out(func):

    def function_in(num):
        print("-------开始验证-------",num)
        func(num)
    return function_in

@function_out
#login = function_out(login)
def login(num):
    print("开始登陆num=",num)


login(10)