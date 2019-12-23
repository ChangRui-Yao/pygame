class Test(object):

    def __init__(self,func):
        print("这是__init__方法")
        print("---------------func------",func)
        #self.func就是这个func的引用
        self.func = func
    def run(self):
        print("这个值正在疯跑")

    def __call__(self,*args,**kwargs):
        print("------call---------")
        self.func()


@Test
def login():
    print("开始登陆")
login()