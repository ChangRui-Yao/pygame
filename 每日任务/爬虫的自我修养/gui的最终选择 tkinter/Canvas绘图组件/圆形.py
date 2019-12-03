from tkinter import *
root = Tk()

w = Canvas(root, width=200, height=100,background="white")#---设置一张画布   长度200  高度100  底色白色
w.pack()



w.create_rectangle(40,20,160,80,dash=(4,4))#---矩形

w.create_oval(70,20,130,80,fill="pink")#-----椭圆   或者   圆形（特殊的椭圆）

w.create_text(100,50,text="姜枫")



mainloop()