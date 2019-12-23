"""
#目标给Login()增加验证功能
#不修改源代码

"""

def functiion_out(func):

    def functiion_in():
        print("开始验证")
        func()
    
    return functiion_in
@functiion_out
#@functiion_out  装饰了login()函数
#底层  login = funcition_out(login)
def login():
    print("开始登陆")



#通过闭包调用外城函数
#login = functiion_out(login)
login()