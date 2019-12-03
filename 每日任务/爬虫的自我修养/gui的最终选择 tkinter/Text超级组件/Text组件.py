#Text组件常用于显示或处理多行文本
#-----非常灵活   常常被当做文本编辑器使用  网页浏览器

from tkinter import *

root = Tk()

text = Text(root,width=30,height=5)#-width =30  相当于30个字符那么宽 height 2行
text.pack()



text.insert(INSERT,"王者\n")#----insert 是插入一句话的意思 \
                            #后面这个INSERT是当前输入符号所在位置\
                            #也可以END  表示最后一位
text.insert(END,"荣耀")


def show():
    print("游戏结束")

b1 = Button(text,text="开始游戏",command=show)#---在这里设置了一个按钮等于b1

text.window_create(INSERT,window=b1)#----如何在文本编辑窗口显示一个按钮
                                    #---window_create(位置,window=b1)


mainloop()
