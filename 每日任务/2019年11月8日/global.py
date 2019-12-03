import os
count = 10

def myfunction():
	#python 调用外部的变量，对它修改，会屏蔽操作
	global count
	count = 20
	
	#----------------内嵌函数-------------------
	def printf(cout):
		#自定义的操作
		print("printf自定义输出:count=%d" %(cout))
	#----------------内嵌函数-------------------
	return printf
	
#第一种调用函数内部的函数
fun=myfunction()     				#count=20
fun(count)
	
#直接用这个函数
myfunction()(count)
