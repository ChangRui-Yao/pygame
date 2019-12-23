def test():
    #        0 1 2 3 4 5 6
    list1 = [1,2,3,4,5,6,7]
    print("list1=",list1,id(list1))
    #切片拷贝
    list2 = list1[:]
    print("list2=",list2,id(list2))


def tses2():
    A = [1,2,3]
    B = [11,22,33]
    C = (A,B)
    print("c=",C,id(C))

    D = C[:]
    print("D=",D,id(D))


dict1 = {"age":[1,2,3]}
print("dict1= ",dict1,id(dict1))

dict2 = dict1.copy()
print("dict2=",dict2,id(dict2))

dict1["age"][0] = 100
print("dict1= ",dict1,id(dict1))
print("dict2=",dict2,id(dict2))