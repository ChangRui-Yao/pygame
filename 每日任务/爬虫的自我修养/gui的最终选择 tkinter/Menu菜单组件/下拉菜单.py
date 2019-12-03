from tkinter import *

root = Tk()
def show():
    print("你好")

def callback():
    print("你好")
menubar = Menu(root)#-----这里是在root界面创建了一个Menu菜单
###########menubar.add_command(label="hello",command=show)
###########menubar.add_command(label="quit",command=root.quit)#------root.quit退出窗口
root.config(menu=menubar)               #--这一句的意思是绑定这个菜单是在menubar这个界面里的
#################################################################################################
filemenu = Menu(menubar,tearoff=True)#-----------filemenu 是在meunbar菜单里边创建了一个菜单
filemenu.add_command(label="打开",command=callback)#--------tearoff 默认等于True 他的作用是 设置这个级联菜单
                                                                #是可以撕开的  等于False就不可以撕开
filemenu.add_separator()                    #--------设置一条分割线
filemenu.add_command(label="保存",command=callback)
filemenu.add_command(label="退出",command=callback)
menubar.add_cascade(label="文件",menu=filemenu)#----------在这里设置他的级联菜单
###############################################################################################
editmenu = Menu(menubar,tearoff=False)#-----------deitmenu 也是在meunbar菜单里边创建了一个菜单
editmenu.add_command(label="剪切",command=callback)                    #--------设置一条分割线
editmenu.add_command(label="拷贝",command=callback)
editmenu.add_command(label="复制",command=callback)
menubar.add_cascade(label="编辑",menu=editmenu)             #------设置他的级联菜单
mainloop()