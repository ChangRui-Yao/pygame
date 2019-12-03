from tkinter import *

root = Tk()
def callback(event):
    print(event.char)#----每一个键的char    就是他本身的名字


frame = Frame(root,width=200,height=200)

frame.bind("<Key>",callback)
frame.focus_set()#------因为一个窗口可能有很多组件 你这个组件想要响应键盘
                #----一次敲击键盘 他不知道是响应那个组件
                #所以你这个组件需要获得焦点  用这个focus_set()一形成就获得焦点
frame.pack()



mainloop()