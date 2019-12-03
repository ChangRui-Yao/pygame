from tkinter import *
root = Tk()


w1 = Message(root,text="这是一则消息",width=100)
w1.pack()

w2 = Message(root,text="这是\n一则咋咋呼呼真好真和就hiuhiuhhihhuh呼呼呼火狐消息",width=100)#-----massage支持自动换行 
                            #--也可以强行要求他换行
w2.pack()

mainloop()