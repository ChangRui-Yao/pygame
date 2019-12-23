def test():
    print("哈哈哈哈我是一个Test")
test()
#函数名是一个特殊的变量
ret = test
print(ret)



#id()获取对象地址
#print("%x" % id(ret))
#print("%x" % id(test))


#通过ret调用函数
ret()
#1)所谓函数名是一个特殊的变量，保存了函数在内存中的首地址
# 2）通过自定义变量可以获取获取函数地址
# 3自定义变量调用函数    “变量名()”   变量名=函数名
name1 = "132"
name2 = "132"
print(id(name1))
print(id(name2))

