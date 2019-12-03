#------------------------------------实现多个选项选择多个
from tkinter import *
##########
##########
##########root = Tk()
##########
##########GIRLS = ["婉儿","韩信","猴子","公孙离"]
##########
##########v = []
##########for girl in GIRLS:
##########    v.append(IntVar())#---------因为每一个元素都是APPEND加进去的  都是最后一个元素
##########    b = Checkbutton(root,text=girl,variable=v[-1])#--------每一次都得拿到他的最后一个元素-1
##########    b.pack(anchor=W)#-------设置左对齐
##########
##########
##########mainloop()
##########



#-------实现多个选择选择一个
root = Tk()

v= IntVar()
def f():
    print(v.get())
Radiobutton(root,text="婉儿",variable=v,value=1,command=f).pack(anchor=W)
Radiobutton(root,text="猴子",variable=v,value=2,command=f).pack(anchor=W)
Radiobutton(root,text="公孙离",variable=v,value=3,command=f).pack(anchor=W)


mainloop()



#-------------如何改变按钮前面的样式
##root = Tk()
##
##group = LabelFrame(root,text="最好的脚本语言是？",padx=100,pady=0)
##group.pack(padx=100,pady=100)
##
##LANGS = [
##    ("python",1),
##    ("婉儿",2),
##    ("韩信",3),
##    ("那谁",4)]
##
##v = IntVar()
##print(v)
###v.set(1)   #-------------默认选择    默认给定set(1)  也就是LANGS里面的python
##for lang, num in LANGS:
##    b = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)#----indicatoron=Fslse是自改按钮前面的小圈 改为选择填充
##    b.pack(anchor=W)#------fill = X  选择横向填充
##
mainloop()
