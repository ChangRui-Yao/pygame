class My_len:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
        self.__str = "123123"


    def get(self):
        return self.__str
    def set(self,name):
        self.__str = name 
    def __len__(self):
        return len(self.values)


    def __getitem__(self,ley):
        self.count += 1 
        return self.values[key]
# ----------类里的成员函数  在调用的时候 会默认添加self参数  因此一般情况下在定义的时候需要添加self
#--------以双下划线开始的成员函数都是魔法函数
#--------在类中的定义的变量都叫做成员变量  在类中定义的函数 都叫做成员函数
#-------类中双下划线开始的变量为私有变量  在其外部无法被访问
#-------调用成员函数时加括号
    def test(self):
        print("这是test函数")
s = My_len(1,2,3)
print(s.values)
s.test()
#print(s.__str)
print(s.get())
s.set("456456")
print(s.get())
