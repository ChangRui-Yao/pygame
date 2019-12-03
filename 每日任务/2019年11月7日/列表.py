#python列表
menber = ['姜枫','婉儿','刘备']
print(menber)

number = [1,'姜枫',3.14,[1,2,3,4]]
#问题（1）如何创建一个空列表
enty = []
#问题（2）如何给列表中添加元素
#(1)
menber.append('孙尚香')
print(menber)
#(2)
menber.extend(["韩信","李白"])
print(menber)
#(3)
menber.insert(1,'公孙离')
print(menber)
#问题（3）如何利用索引值进行交换元素位置
temp = menber[0]
menber[0] = menber[1]
menber[1] = temp
print(menber)
#问题（2）如何删除元素
#(1)
menber.remove('姜枫')
print(menber)
#(2)
del menber[1]
print(menber)
#(3)
name = menber.pop(2)
print(menber)
#切片
qiepian = menber[1:3]
print(qiepian)




