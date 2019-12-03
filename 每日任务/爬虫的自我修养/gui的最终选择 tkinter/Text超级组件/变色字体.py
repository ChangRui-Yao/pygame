from tkinter import *
import webbrowser   #---用于打开网页的一个成熟的模块
root = Tk()

text = Text(root,width=30,height=5)
text.pack()




text.insert(INSERT,"王者荣耀之上官婉儿132465464")
#----tag支持事件绑定,比如用鼠标点击 他会进入一个网站


text.tag_add("link","1.7","1.16")
text.tag_config("link",foreground="blue",underline=True)

def show_arrow_cursor(event):#-----绑定时必须加上一个event参数
    text.config(cursor="hand2")#--设置他的鼠标为arrow
    text.tag_config("link",foreground="red")
def show_xtrem_cursor(enent):
    text.config(cursor="xterm")#--回调函数  离开他  又设置为xtrem
    text.tag_config("link",foreground="blue")
def clikc(enent):
    #webbrowser.open("http://www.baidu.com")
    print("123")




text.tag_bind("link","<Enter>",show_arrow_cursor)#--这句话的意思是事件绑定
                    #--这里这个Enter 是当鼠标进入这个tag也就是link
                    #--就调用之后的这个函数

text.tag_bind("link","<Leave>",show_xtrem_cursor)#---如果离开这里就调用跟那个函数

text.tag_bind("link","<Button-2>",clikc)#---如果左键点击就调用后面的这个click
                                #---用于打开网页  则需要调用webbrowser
mainloop()
