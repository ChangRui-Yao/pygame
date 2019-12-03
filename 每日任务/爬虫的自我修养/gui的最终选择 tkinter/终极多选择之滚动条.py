from tkinter import *

master = Tk()

sb = Scrollbar(master)#这两句设置了一个空白的滚动条
sb.pack(side=RIGHT,fill=Y)#设置滚动条位置


theLB = Listbox(master,yscrollcommand=sb.set)            # selectmode=SINGLE只能单选一个
                                    #selectmode=BROWSE  也是只能选择一个  但是拖动鼠标或者通过方向键可以改变选项  默认的话是这个
                                     #selectmode=MULTIPLE  多选
                                      #selectmode=EXTENDED 也是多选 但是得同时按住shift或者ctrl或拖动鼠标实现

                            #height=11
theLB.pack()

for item in range(1000):
    theLB.insert(END,item)    #----END表示最后一个的位置




theButton = Button(master,text="删除它",\
                   command=lambda x=theLB:x.delete(ACTIVE))#---这里用了lambda表达式   delete 删除元素   ACTIVE表示当前选中的值

theButton.pack(side=LEFT,fill=BOTH)

sb.config(command=theLB.yview)#----------这一句表示前后互通

mainloop()






#---------------如果需要显示很多选项    但是他这里默认只显示9行  怎么操作
                #1修改他的height 参数
                #2给他加上一个滚动条    滚动条作为一个独立的组件
                        #1设置该组件的yscrollcommand选项为Scrollbar组件的set()方法
                        #设置Scrollbar组件的command选项为该组件的yview()方法
