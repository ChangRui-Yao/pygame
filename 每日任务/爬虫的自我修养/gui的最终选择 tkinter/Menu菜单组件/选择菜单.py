from tkinter import *
#------如果说着里有一个列表或者元组’
OPTIONS = ["上官婉儿","韩信","李白","元歌","鲁班","橘子"]
root = Tk()

variable = StringVar()
#variable.set("ONE")#------这里she值得是一个默认值
variable.set(OPTIONS[0])

w = OptionMenu(root,variable,*OPTIONS)#----------*号这里是一个可变参数  因为OPTIONS是一个列表  
                                        #如何将列表中的元素穿进去  而不是 列表 
                                        #哦！原来*号还具有解包的功能  nice
w.pack()


mainloop()