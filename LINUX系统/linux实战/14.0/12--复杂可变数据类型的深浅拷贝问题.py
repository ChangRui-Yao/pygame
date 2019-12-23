import copy
def l1():
    A=[1,2,3]
    B=[11,22,33]
    C=[A,B]

    print("A=",A,id(A))
    print("B=",B,id(B))
    print("C=",C,id(C))
    print("C[0]",C[0],id(C[0]))



    D=copy.copy(C)
    print("D=",D,id(D))
    print("D[0]=",D[0],id(D[0]))
    print("D[1]=",D[1],id(D[1]))

A=[1,2,3]
B=[11,22,33]
C=[A,B]

print("A=",A,id(A))
print("B=",B,id(B))
print("C=",C,id(C))
print("C[0]",C[0],id(C[0]))



D=copy.deepcopy(C)
print("D=",D,id(D))
print("D[0]=",D[0],id(D[0]))
print("D[1]=",D[1],id(D[1]))
