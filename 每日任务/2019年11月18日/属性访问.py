###--这里定义一个类  这个类继承内置函数int
##class int(int):
##    #-----如果使用这个类里的魔法方法
##    def __add__(self,other):
##        #----就会返回int.__sub__  也就是剪发
##        return int.__sub__(self,other)
##a = int("5")
##b = int("3")
##print(a + b)



#______________________________________________
#----什么是反运算
class Nint(int):
    def __radd__(self,other):
        return int.__sub__(self,other)
a = Nint(5)
b = Nint(3)
#---在这里1没有找到?????
print(a + b)
print(1 + b)


#--------------属性访问见计时器.py


