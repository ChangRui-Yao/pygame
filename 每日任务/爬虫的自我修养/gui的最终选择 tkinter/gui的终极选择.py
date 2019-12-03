#gui的终极选择   TKinter
import tkinter as tk            #_---生成了一个顶层窗口的实例 TK
app = tk.Tk()

            
app.title("王者荣耀")           #---设置他的标题 title


theLabel = tk.Label(app, text = "我的第二个窗口程序")#----Label主要用于显示文本  图标 组件
theLabel.pack()             #------pack   自动调节图标 文本的尺寸



app.mainloop        #-----主序界循环开始   基本是图形程序的最后一句

