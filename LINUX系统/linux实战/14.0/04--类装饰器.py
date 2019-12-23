class Test(object):

    def __init__(self):
        print("这是__init__方法")

    def run(self):
        print("这个值正在疯跑")

    def __call__(self,*args,**kwargs):
        print("------call---------")

#创建对象
test = Test()
#test.run()
#当类对象后面加上括号，就会去调用这个类中的__call__()方法
test()