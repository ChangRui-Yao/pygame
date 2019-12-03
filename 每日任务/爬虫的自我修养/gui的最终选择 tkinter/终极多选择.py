from tkinter import *

master = Tk()

theLB = Listbox(master)            # selectmode=SINGLE只能单选一个
                                    #selectmode=BROWSE  也是只能选择一个  但是拖动鼠标或者通过方向键可以改变选项  默认的话是这个
                                     #selectmode=MULTIPLE  多选
                                      #selectmode=EXTENDED 也是多选 但是得同时按住shift或者ctrl或拖动鼠标实现
theLB.pack()

for item in ["婉儿","李白","韩信","王昭君"]:
    theLB.insert(END,item)    #----END表示最后一个的位置


theButton = Button(master,text="删除它",\
                   command=lambda x=theLB:x.delete(ACTIVE))#---这里用了lambda表达式   delete 删除元素   ACTIVE表示当前选中的值

theButton.pack()



mainloop()
