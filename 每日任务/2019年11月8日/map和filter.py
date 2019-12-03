#-------filter------可以起一个过滤器的作用,配合lambda使用----
list(filter(None,[1,0,False,True]))

def odd(x):
    return x % 2
temp = range(10)

show = filter(odd,temp)

print(list(show))
#--------------上面这一堆可以简化为--------
print(list(filter(lambda x : x % 2 ,range(10))))

#----------------map()---------将序列的每一个参数进行加工并返回一个新序列
print(list(map(lambda x : x * 2,range(10))))

 
