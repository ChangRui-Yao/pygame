#-------判断文本的md5  摘要 判断用户是否发生改变
from tkinter import *
import hashlib  #---想要获得md5的值需要调用的必须
root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"王者荣耀之上官婉儿132465464")
#----tag支持事件绑定,比如用鼠标点击 他会进入一个网站
contents = text.get("1.0",END)
def getsig(contents):
    m = hashlib.md5(contents.encode())      #-------传入这个数据   encode对它进行进制转换
    return m.digest()   #_----------获得他的摘要
sig = getsig(contents)
def check():
    contents = text.get("1.0",END)
    if sig != getsig(contents):
        print("发生改变")
    else:
        print("未发生改变")

Button(root,text="判断",command=check).pack()

mainloop()
