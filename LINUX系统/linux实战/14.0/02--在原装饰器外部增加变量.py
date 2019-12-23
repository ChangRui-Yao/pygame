"""
1)存在闭包
#2)存在待装饰的函数

"""
def test(path):
    print(path)
    def function_out(fucc):
        print("------function_out-------",path)
        def function_in():
            print("------开始验证------")
            fucc()

        return function_in
    #test返回装饰器的引用  装饰器工厂模式
    return function_out



@test("login.py")
#分解为两部
#先执行test("login.py")
#@第一布的结果

#@funciton_out
#login = funcition_out(login)
def login():
    print("开始登陆")

#@test("register.py")
#def register():
#    print("-----开始注册-------")


login()
#register()