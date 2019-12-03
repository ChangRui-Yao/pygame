def ds():
	return 2 * x + 1

#--改成lambda表达式----

lambda x : 2 * x + 1
g = lambda x : 2 * x + 1
print(g(5))


#-----------(1)使用lambda可以使代码更加简洁------


def add(x,y):
       return x + y

#--改成lambda表达式--------

lambda x, y : x + y
p = lambda x, y : x + y
print(p(3,4))
-------------#




#--------------------(2)是用lambda不用考虑命名问题-------
#--------------------(3)简化代码的可读性，不需要到def部分-------
