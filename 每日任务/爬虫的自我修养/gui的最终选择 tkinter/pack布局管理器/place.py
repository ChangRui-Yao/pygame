from tkinter import *
root = Tk()

photo = PhotoImage(file="G:\PersonPro\PythonPro\每日任务\爬虫的自我修养\gui的最终选择 tkinter\pack布局管理器\jj.gif")
Label(root,image=photo).pack()


def show():
    print("正中靶心")


Button(root,text="点我",command=show).place(relx=0.5,rely=0.5,anchor=CENTER)
#-------relx0.5.rely=0.5 表示在中间    0表示左边   1表示右边  anchor=CENRER  表示居中显示

mainloop()