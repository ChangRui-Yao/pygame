#对象 = 属性 + 方法

#OOA    面相对象分析
#OOP    面向对象编程
#OOD    面向对象设计


#------面向对象的几个特征
		#封装----对外部隐藏对象的工作细节
		#继承----子类自动共享父类之间数据和方法的机制
		#多态----可以对不同类的对象条用相同的方法，产生不同的结果






#1-------什么是self
class Ball:
    def setName(self,name):
        self.name = name

    def kick(self):
        print("我叫%s,该死的 谁踢我0 " % self.name)

#__init__()
        #------构造函数
    
        
