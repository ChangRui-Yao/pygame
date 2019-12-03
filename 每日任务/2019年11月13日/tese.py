#--------try 语句 一旦发现异常  接下来的不会被执行
try:
    sum = 1 + '1'
    f = open('文件.txt')
    print(f.read())
#---------------如果出错应该怎么做
except OSError as reason:
    print("文件出错了\n错误的原因是:"+ str(reason))
except TypeError as reason:
     print("类型 出错了\n错误的原因是:"+ str(reason))

             #--------finally:无论如何都会被执行的代码
     
finally:
      f.close()


            #---------如何自己引出一个异常
raise 
