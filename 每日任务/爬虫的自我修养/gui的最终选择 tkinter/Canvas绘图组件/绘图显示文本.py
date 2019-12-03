from tkinter import *
root = Tk()

w = Canvas(root, width=200, height=100,background="white")#---设置一张画布   长度200  高度100  底色白色
w.pack()


w.create_line(0,0,200,100,fill="green",width=3)#----设置线的初始宽度为3    #
w.create_line(200,0,0,100,fill="green",width=3)
w.create_rectangle(40,20,160,80,fill="green")

w.create_rectangle(65,35,135,65,fill="yellow")
w.create_text(100,50,text="姜枫")#-------这里显示文本 默认100.50是这个root的正中间
                                    #----如果要靠左或者靠右  



mainloop()