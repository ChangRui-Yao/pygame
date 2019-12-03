from tkinter import *
import tkinter.messagebox
from tkinter import colorchooser

root = Tk()

def show():
    fileName = colorchooser.askcolor()
    print(fileName)
                                        #-----筛选打开文件的格式
    print(fileName)






Button(root,text="选择颜色",command=show).pack()
mainloop()