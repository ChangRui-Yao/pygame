from tkinter import *

root = Tk()
def show():
    print("你好")


menubar = Menu(root)
menubar.add_command(label="hello",command=show)
menubar.add_command(label="quit",command=root.quit)#------root.quit退出窗口


root.config(menu=menubar)#----在这里菜单实例虽然有了  没有把他添加到root窗口上
                        #---root窗口有一个menu菜单  使用config把他们关联上去
                        #--这里直接添加到主菜单上  不是窗口菜单


mainloop()