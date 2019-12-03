#设置撤销功能
from tkinter import *
import hashlib  #---想要获得md5的值需要调用的必须
root = Tk()

text = Text(root,width=30,height=5,undo=True,autoseparators=False)#------在这里必须打开他的undo  默认为False
                                #_-有一个自以为是的做法就是他默认这句话是没有结束的 一次撤销所有的输入就都没了
                                #-在这里可以设置他的autoseparators=Fslse
text.pack()
text.insert(INSERT,"王者荣耀之上官婉儿132465464王王王王")
def callback(event):
    text.edit_separator()

text.bind('<Key>',callback)#----定义每当有一个按键输入  就插入一个分隔符 也就是说每次输入 都算一个栈
def show():
    text.edit_undo()#------如果点击这个按钮  则撤销操作
Button(root,text="撤销",command=show).pack()




mainloop()