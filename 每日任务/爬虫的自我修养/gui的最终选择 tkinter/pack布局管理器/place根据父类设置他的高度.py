from tkinter import *
root = Tk()


Label(root,bg="red").place(relx=0.5,rely=0.5,relheight=0.75,relwidth=0.75,anchor=CENTER)
#-------relx0.5.rely=0.5 表示在中间    0表示左边   1表示右边  anchor=CENRER  表示居中显示
Label(root,bg="blue").place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5,anchor=CENTER)
Label(root,bg="green").place(relx=0.5,rely=0.5,relheight=0.25,relwidth=0.25,anchor=CENTER)
mainloop()              #-----relheight=0.25,relwidth=0.25sh设置相对他的父组件的位置