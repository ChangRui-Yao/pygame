import easygui as g
import sys
#tile = g.fileopenbox("急急急","wwwwwww","G:\PersonPro\PythonPro\每日任务\*.py",["*.css", ["*.htm", "*.html", "HTML files"],"*.txt",["*.dev","dev files"]],True)
#print(tile)
test = TextBox("jjjjjiji")
print(type(test.text()))
while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

    msg ="请问你的理想是什么?"
    title = "小游戏互动"
    choices = ["科学家","教师","流氓","程序猿"]

    choice = g.choicebox(msg,title,choices)


    g.msgbox("你的选择是："+ str(choice),"结果")

    msg = "你希望重新开始小游戏吗?"
    title = "请选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
