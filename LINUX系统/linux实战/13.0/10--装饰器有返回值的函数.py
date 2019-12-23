
def functiion_out(func):

    def functiion_in(num):
        print("开始验证")
        return func(num) 
    return functiion_in
@functiion_out
def login(num):
    print("开始登陆")
    return num + 10



result = login(8)
print(result)