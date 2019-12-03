from tkinter import *

root = Tk()

text = Text(root,width=30,height=5)
text.pack()




text.insert(INSERT,"王者荣耀之上官婉儿132465464")

text.tag_add("tag1","1.5","1.9") #--这里添加了一个tag1，从第一行第五列,到第一行第九列

text.tag_add("tag2","1.5","1.9")



text.tag_config("tag1",background="yellow",foreground="red",underline=True)#--背景色等于黄色,前景色等于blue
                                                #---underline=True给这一段tag1下面加上一个下划线   默认这个值是False


text.tag_config("tag2",background="red",foreground="blue")#-------如果有多个tag绑定着几个字符 那么后来的会覆盖前面的
                                    #-----可以使用tag_ralse()和tag_lower()提高或者降低优先级
text.tag_lower("tag2")




#----tag支持事件绑定,比如用鼠标点击 他会进入一个网站






mainloop()
