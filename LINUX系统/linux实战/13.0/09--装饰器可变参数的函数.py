def function_out(func):

    def function_in(*args,**kwargs):
        print("-------开始验证-------")
        print("-------args----",args)
        print("------kwargs----",kwargs)
        func(*args,**kwargs)
    return function_in

@function_out
#login = function_out(login)
def login(*args,**kwargs):
    print("开始登陆num=")
    print("-------args----",args)
    print("------kwargs----",kwargs)


login(10,a=10)