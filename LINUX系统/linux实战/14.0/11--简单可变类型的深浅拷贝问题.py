import copy

list1 = [1,2,3]
print("list=",list1,id(list1))

list2 = copy.copy(list1)
print("list2=",list2,id(list2))

list2.append(4)
print("新list1=",list1,id(list1))
print("新list2=",list2,id(list2))