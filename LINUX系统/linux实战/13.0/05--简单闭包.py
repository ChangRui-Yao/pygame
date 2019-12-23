def funcity_out(num):

    print("1funcity_out num =",num)

    def funcity_in(num_in):
        print("2.-------funcity_in-----------num",num)
        print("3.-------funcity_in-----------num_in=", num_in)
    
    return funcity_in

#funcity_out(10)
#调用 funcity_out   获取内层函数地址保存到变量中
ret = funcity_out(100)
ret(88)