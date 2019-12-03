count = 5
def my_gaobal():
        #--------------先声明在此修改全局变量count函数--------
	global count
	#-------------重新定义count------------
	count = 10
	#
	print(count)
my_gaobal()
