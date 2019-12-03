def funx(x):
	def funy(y):
		return x * y
	return funy
i = funx(8)
i(5)
fun(8)(5)