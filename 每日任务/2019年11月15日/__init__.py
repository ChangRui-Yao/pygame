class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我" % self.name)
b = Ball()
b.kick()


#-------公有和私有
class Person:
    name = "姜枫"

        #-----在这里name就是公用的
p = Person
p.name

        #---定义私有   在其前面加上__双下划线
class Person:
    __name = "姜枫"
    def getName(self):
        return self.__name

p = Person
p.gerName
