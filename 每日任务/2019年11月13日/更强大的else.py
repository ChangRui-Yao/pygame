#else   不止和if进行判断 还可以和while   for配合使用   循环结束才能使用
            #要么怎样 要么怎样
            #干完了怎么样   干不完怎么样
            #没有问题  那就干吧
def sushu(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d的最大约数是%d" % (num,count))
            break
        count -= 1
    else:
        print("%d是素数" % num)
num = int(input("请输入一个数:"))
sushu(num)

