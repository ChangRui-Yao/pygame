#-------内嵌函数-------
def fun1():
	print("fun1正在被调用")
	def fun2():
		print("fun2正在被调用")
		#注意此处此处缩进
	fun2()
fun1()
