from tkinter import *
root = Tk()
w = Canvas(root,width=400,height=200,)
w.pack()
def paint(event):
    x1,y1 = (event.x - 1),(event.y - 1)
    x2,y2 = (event.x + 1),(event.y + 1)
    w.create_oval(x1,y1,x2,y2,fill = "red")


w.bind("<B1-Motion>",paint)
Label(root,text="拖动鼠标绘制你的理想").pack(side=BOTTOM)#----位置底部




#---很遗憾python是没有 获得用户鼠标当前点击的位置    来画一个点的
# -----或的当前点击位置  得到他的参数 绘制一个贼小的椭圆  将他们连起来 就得到一个类似于画板的东西 




mainloop()