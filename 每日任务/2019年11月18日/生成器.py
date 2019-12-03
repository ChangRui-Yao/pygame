def Mygen():
    print("生成器被执行")
    
    for i in range(10):
        #print(i)
        yield i

t = Mygen()


e = (i for i in range(10))

#for i in range(10):
 #   print(i)
