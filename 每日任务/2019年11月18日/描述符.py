class s:
    def __get__(self,instance,owner):
        #--第一个参数self就是描述符类他本身的实例
        #--第二个参数就是他的拥有者的这个类的实例
        #--第三个参数是他的拥有者的本身
        print("get正在被使用",self,instance,owner)


    def __set__(self,instance,value):
        print("set正在被调用",self,instance.vanlue)
        #---第三个是等号右边的参数

    def __delete__(self,instance):
        print("delete正在被调用",self,instance)

class Test:

    #-----在这里s类里面定义了描述符许阿姨的魔法方法
    #-----x = s()   把s类的实例赋值给x
    #_____所以s就被称作x的描述符类
    x = s()
