#------递归算法-----
#def recursion():
#	return recursion()
#recursion()
	
	
#------如何设置递归深度----
#import sys
#sys.setrecursionlimit(深度)
#--------递归求阶乘
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
number = int(input("请输入一个正整数："))
result = factorial(number)
print("%d 的阶乘是 %d " % (number,result))
 
	
