"""
#类名，Page
#初始化方法
#获取开始的位置
#获取结束的位置


"""
class Page(object):

    def __init__(self,num):
        #保存当前页
        self.current_page = num
        #每页大小
        self.pagesize = 10
    @property
    def start(self):
        #limit(当前页-1)*每页大小,每页大小
        #1,10       11,20
        return (self.current_page - 1)*10 + 1
    @property
    def end(self):
        return self.current_page * self.pagesize

page1 = Page(1)
#print(page1.start())
#print(page1.end())

print(page1.start)
print(page1.end)