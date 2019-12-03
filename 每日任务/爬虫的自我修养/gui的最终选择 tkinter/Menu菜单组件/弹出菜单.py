from tkinter import *

root = Tk()

def callback():
    print("你好")
menubar = Menu(root)#-----这里是在root界面创建了一个Menu菜单

#root.config(menu=menubar)               #--这一句的意思是绑定这个菜单是在menubar这个界面里的
#################################################################################################
filemenu = Menu(menubar,tearoff=False)#-----------filemenu 是在meunbar菜单里边创建了一个菜单
filemenu.add_command(label="打开",command=callback)             
filemenu.add_command(label="保存",command=callback)
filemenu.add_command(label="退出",command=callback)
menubar.add_cascade(label="文件",menu=filemenu)#----------在这里设置他的级联菜单
frame = Frame(root,width=512,height=512)
frame.pack()
def popup(event):
    filemenu.post(event.x_root,event.y_root)

frame.bind("<Button-3>",popup)


mainloop()