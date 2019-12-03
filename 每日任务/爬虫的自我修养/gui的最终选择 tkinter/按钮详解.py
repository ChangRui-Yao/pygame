from tkinter import *
def callback():
    var.set("信你个龟")

root = Tk()
#--------在这里搭建了两个框架
frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()
var.set("你所下载的影片有限制内,\n请满十八岁后观看!")
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT,)#-----左对齐
textLabel.pack(side=LEFT)


        #-----实例化PhotoImage(file="路径")
photo = PhotoImage(file="jj.gif")
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)#-----------设置右对齐



theButton = Button(frame2,text="我已满18周岁", command=callback)


theButton.pack()
frame1.pack(padx=10,pady=10)#----边界为10xy轴
frame2.pack(padx=10,pady=10)
mainloop()
