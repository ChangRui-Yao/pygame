"""
#创建一个生成器
    #目标：实现斐波那契数列
    #1)定义变量保存第一列和第二列的值
    #2）定义变量保存当前生成的位置


    #3）循环生成数据  条件是当前列数《总列数
    #4）保存a的值
    #5）修改a  \ b 的值
    #6）返回a的值   使用yield

#2定义变量 保存生成器
#next(生成器)得到下一个元素值
"""
#创建一个生成器
def fibnacci(n):
    #目标：实现斐波那契数列
    #1)定义变量保存第一列和第二列的值
    a = 1
    b = 1
    #2）定义变量保存当前生成的位置
    weizhi = 0
    print("-------------------111111111----------------")

    #3）循环生成数据  条件是当前列数《总列数
    while weizhi < n :
        #4）保存a的值
        data = a
        #5）修改a  \ b 的值
        a,b = b, a + b
        #列数加1
        weizhi += 1
        #6）返回a的值   使用yield
                #yield的作用：
                #能够充当return的作用
                #能够保存程序的运行状态，并且暂停程序的执行
                #当next()的时候，可以继续唤醒程序从yield位置往下执行
        print("-------------222222222--------------")
        XXX = yield data
        print("--------------3333333--------------------")
        if XXX == 1:
            #生成器可以使用return，让生成器结束
            return "哈哈，我是return，我能让生成器结束"

#2定义变量 保存生成器
if __name__ == "__main__":
    fib = fibnacci(5)
#next(生成器)得到下一个元素值
    value = next(fib)
    print("第1列",value)
    try:
        value = next(fib)
        print("第2列",value)

        value = fib.send(1)
        print("第3列",value)
    except Exception as e:
        print(e)