#import module1
#module1模块名    name是一个变量
#print(module1.name)


#查看系统的path环境变量
#导入模块
#打印路径
import sys
for p in sys.path:
    print(p)
print("--"*20)
    #把指定的目录加入到环境变量中,追加到末尾
#sys.path.append("C:/Users/lenovo/Desktop/test")
    #追加到开头
sys.path.insert(0,"C:/Users/lenovo/Desktop/test")
print(sys.path)

import app
print(app.name)