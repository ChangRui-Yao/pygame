try:
    f = open('data.txt','w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print("出错啦" + str(reason))
finally:
    f.close()
#------改为with的格式
try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("出错啦" + str(reason))
