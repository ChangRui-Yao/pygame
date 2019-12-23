"""
可变：变量创建完成后，内存内容可以再改变
不可变：变量创建，内存一旦分配完成后，就不能在改变了
a变量，保存数字，不可变的
"""
a = 10
print(id(a))

b = a + 1
print(id(b))


list1 = [1,2,3]
print("list1",id(list1))
list2 = list1
print("--------list2-----",id(list2))
list2.append(9)
print(id(list2))