from tkinter import *


root = Tk()


textLabel = Label(root,
                  text="你所下载的影片有限制内,\n请满十八岁后观看!",
                  justify=LEFT,#-----左对齐
                  padx=10)#----边界为10
textLabel.pack()


        #-----实例化PhotoImage(file="路径")
photo = PhotoImage(file="jj.gif")
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)#-----------设置右对齐



mainloop()
