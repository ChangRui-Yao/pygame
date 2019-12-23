#装饰器不修改源代码   增加新的功能
from contextlib import contextmanager
#装饰器装饰函数的步骤
@contextmanager
def myopen(file_name,file_model):
    print("进入上文")
    file = open(file_name,file_model)
    yield file
    print("进入下文")
    file.close()


with myopen("G:/GitPro/pygame/LINUX系统/linux实战/15.0/1.txt","r") as file:
    file_data = file.read()
    print(file_data)