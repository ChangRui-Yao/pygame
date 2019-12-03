from tkinter import *
import math as m   #------要使用到sin  cos  tan需要这个模块
root = Tk()

w = Canvas(root, width=200, height=100,background="red")#---设置一张画布   长度200  高度100  底色白色
w.pack()

center_x = 100
center_y = 50
r = 50


points = [\
    #左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #左下点
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    #顶点
    center_x,
    center_y - r,
    #右下点
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5))
    ]
w.create_polygon(points,outline="green",fill="yellow")#----多边形  给他点的顺序  自己会发出一条直线 将他们连接
                        #--fill 颜色属性 只有当他形成一个闭合图形 才会出现 颜色填充
                        #--默认黑色填充   如果不给指定颜色  给他一个空的   透明色


mainloop()