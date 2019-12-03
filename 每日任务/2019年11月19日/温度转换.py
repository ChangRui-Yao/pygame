###-------这是一种调用模块方法   直接import加上模块名
##import M1.wendu
##print("32摄氏度 = %.2f华氏度" % wendu.c2f(32))
##print("99华氏度 = %.2f摄氏度" % wendu.f2c(99))
##
##
##
###------第二种    from 模块名 import  函数名
##from M1.wendu import c2f,f2c
##print("32摄氏度 = %.2f华氏度" % c2f(32))
##print("99华氏度 = %.2f摄氏度" % f2c(99))


#-----第三种  import 模块名 as 新名字
import M1.wendu as tc
print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))

