from tkinter import *


root = Tk()

photo = PhotoImage(file="jj.gif")
theLabel = Label(root,
                 text="一二三一二三",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,)#--------设置混合模式就是字体在图片上面
##                 font=("微软雅黑",20)
##                 fg="blue")#设置字体


theLabel.pack()
mainloop()


