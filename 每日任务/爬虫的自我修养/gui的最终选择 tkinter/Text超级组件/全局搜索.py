#-------判断文本的md5  摘要 判断用户是否发生改变
from tkinter import *
import hashlib  #---想要获得md5的值需要调用的必须
root = Tk()

text = Text(root,width=30,height=5)
text.pack()
#s = input("请输入要查找的字符串:")
text.insert(INSERT,"王者荣耀之上官婉儿132465464王王王王")
def getIndex(text,index):
    return tuple(map(int,str.split(text.index(index),".")))
            #---返回 这个元组  
                #-这个元组中map 是表示把切片后的每一个字符串都改成int格式
                #  str.split 表示分割传进来的这个index 分割符为.
start = "1.0"
while True:
    pos = text.search("王",start,stopindex=END)#-----搜索方法一直循环 搜索的字符串 开始位置 结束位置
                                            #--Search方法返回的是一个索引  我们需要把索引转化人类能看懂的形式
    if not pos:
        break
    print("找到了位置是",getIndex(text,pos))#----getIndex 只是将这个值进去 
                    #将这个值转换为默认的行列需要用到index
    #print(pos)
    start = pos +"+1c"          #---+1c表示如果找到字符串就将pos转向下一个字符
mainloop()