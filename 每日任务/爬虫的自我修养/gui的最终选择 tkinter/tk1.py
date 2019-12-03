import tkinter as tk


class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=10,pady=10)
        #------在这里用LEFT设置他出现的位置

                                #----Button  设置一个按钮   frame按钮显示什么字体  bg背景色什么色   fg字体什么颜色, command =他就是如果点击他会出现执行哪些方法
        self.hi_there = tk.Button(frame,text = "打招呼",bg="black",fg="white",command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("大家好啊啊啊啊啊啊")




root = tk.Tk()
app = APP(root)


root.mainloop()
