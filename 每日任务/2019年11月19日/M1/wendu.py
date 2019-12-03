def c2f(cel):
    fah = cel * 1.8 + 32
    return fah


def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

#------------在这里定义了一个测试的函数
def test():
    print("测试，0摄氏度 =%.2f华氏度"% c2f(0))
    print("测试，0华氏度 = %.2f摄氏度"% f2c(0))



#_--------下面这句话如果在函数内部__name__  他就会等于__main__

    #-------如果整个模块被其他模块调用   __name__  就是他自己的函数名

if __name__ == "__main__":
    test()
    
