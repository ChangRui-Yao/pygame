from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

root = Tk()

def show():
    fileName = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GIF",".gif"),("Python",".py")])
                                        #-----筛选打开文件的格式
    print(fileName)






Button(root,text="打开文件",command=show).pack()
mainloop()