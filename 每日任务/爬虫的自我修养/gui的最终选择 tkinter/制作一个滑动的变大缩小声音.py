from tkinter import *

root = Tk()

#----这个组件有两个参数  一个from一个to
        #因为from是python的关键字 所以在这里使用from_ 
s1 = Scale(root,from_=0,to=100,tickinter=20,resolution=5,length=200)
                #--还可以再这里设置他的刻度tickinter=5
                #               设置他的步长resolution=5  就是每次点击自动跳5格
                #    以及设置的他的长度为200像素  length=200           
s1.pack()








s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL,tickinter=20,length=600)
        #-#---默认每一个scale都是垂直的 在这里可以修改他的orient=HORIZONTAL
s2.pack()

def show():
    print(s1.get(),s2.get())


Button(root,text="获取位置",command=show).pack()


mainloop()
