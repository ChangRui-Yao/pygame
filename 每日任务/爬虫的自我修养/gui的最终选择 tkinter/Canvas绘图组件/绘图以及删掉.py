from tkinter import *
root = Tk()

w = Canvas(root, width=200, height=100,background="white")#---设置一张画布   长度200  高度100  底色白色
w.pack()


line1 = w.create_line(0,50,200,50,fill="yellow")    #--定义一条直线 位置参数 0,50,这个点  到200,50 颜色yellow
line2 = w.create_line(100,0,100,100,fill="red",dash=(4,4))#---顶以一条直线 dash = (4,4)  表示虚线 
rext1 = w.create_rectangle(50,25,150,75,fill="blue")#---定义一个矩形 矩形位置

#----要修改他们的方法有三种
w.coords(line1,0,25,200,25)#----coords 直接画布对象 位置
w.itemconfig(rext1,fill="red")#---itemconfig修改的是他的选项  fill = "red"
w.delete(line2)#----删掉某个对象  delete
Button(root,text="删掉全部",command=(lambda x=ALL: w.delete(x))).pack()#---ALL实际上就是一个text 
                                    #---这个lambda表达式就是删掉这个画布上的所有对象

mainloop()