import random
import easygui as g

g.msgbox("嗨,欢迎进入猜数字小游戏^_^")
secret = random.randint(1,10)

msg = "不妨猜一下心里想的是哪一个数字(1~10):"
title = "数字小游戏"
guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
print(type(guess))

while True:
    if guess == secret:
        g.msgbox("卧槽真聪明")
        g.msgbox("可是,猜中了也没有奖励")
        break

    else:
        if guess > secret:
            g.msgbox("大了大了~~~~")
        else:
            g.msgbox("小了小了~~~~")
    guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)


g.msbox("游戏结束不玩了")
            
