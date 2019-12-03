#Text组件常用于显示或处理多行文本
#-----非常灵活   常常被当做文本编辑器使用  网页浏览器

from tkinter import *

root = Tk()

text = Text(root,width=30,height=60)#-width =30  相当于30个字符那么宽 height 60行
text.pack()

photo = PhotoImage(file="jj.gif")       #--如何导入一张图片

def show():
    text.image_create(INSERT,image=photo)       #---如果点击按钮  则添加一张图片

b1 = Button(text,text="开始游戏",command=show)#---在这里设置了一个按钮等于b1

text.window_create(INSERT,window=b1)#----如何在文本编辑窗口显示一个按钮
                                    #---window_create(位置,window=b1)


mainloop()
