import random as r
class Fishee:
    _name = "1223"
    
    
    def __init__(self,name):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)


    def eat(self):
        print("这是Fish的eat函数")


    def move(self):
        self.x -= 1
        print("我的位置是",self.x, self.y)



class Goldfish(Fishee):
    pass
class Carp(Fishee):
    pass
class Salmon(Fishee):
    pass



#---------1调用未绑定的父类方法
                #---2使用super函数
class Shark(Fishee):
    def __init__(self):


       # Fish.__init__(self)
        #------------或者直接添加需要的父类的函数super().__init__()
        #-----用super 方法  以后修改类名字  不需要一个一个修改

        self.hungry = True
    def eat(self):
        Fishee.eat(self)
        super().eat()
        if self.hungry:
            print("吃货的梦想就是天天有的吃")
            self.hungry = False
        else:
            print("吃不下了")
s = Shark()
s.eat()
print(s._name)
