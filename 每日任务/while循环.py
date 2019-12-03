import os
def showListData():
    names = ['xuhang','wangshan','jiangfeng']
    for name in names:
        print(name)
    print("for is down")

#for 关键词: continue break
#break  t退出这个循环
#contie  继续执行循环，但是会掠过下面的语句
def addNumber(x,y):
    print("x= ",x," y= ",y)
    addresoult = 0
    for i in  range(0,x):
        addresoult = addresoult + i
        print(addresoult)
    print("result = " , addresoult)


def showContinue():
    for i in range(0,3):
        print("执行第：",i,"此")
        if i == 1:
            #continue
            break #跳出循环
        print("执行下面的语句：i = ",i)
showContinue()
#showListData()
#addNumber(100,6)
