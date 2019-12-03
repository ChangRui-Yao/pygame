def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("请输入一个人正整数："))
result = factorial(number)
print("%d 的阶乘是%d" % (number,result))
#------递归的两个条件----------
#------(1)调用函数自身---------
#------(2)设置正确的返回值-----
