dict1 = dict.fromkeys(range(5),'人')
#----keys的作用
        #-----他可以将字典中的键访问出来
print(dict1)
for eackeys in dict1.keys():
    print(eackeys)
#---values的作用
        #-----他可以将字典中的值访问出来
for eackeys in dict1.values():
    print(eackeys)
#---items的作用
        #-----他可以将字典中的每一项打印出来  用一个元组的形式
for each in dict1.items():
    print(each)



#get方法会返回一个None-----------
print(dict1.get(6))
#如果不确定 这个键是否存在字典可以用成员资格操作符----
6 in dict1

#-----------------pop-----
            #----------会弹出一个项
print(dict1.pop(2))

#-----------popitem----
            #-----------随机弹出一项
print(dict1.popitem())

#----------update-------
            #----------用字典更新字典
b = {'4':'狗'}
dict1.update(b)
print(dict1)

#-----------------清空字典--------------
dict1.clear()
print(dict1)



#----------------字典中的每一项是没有顺序的-----
