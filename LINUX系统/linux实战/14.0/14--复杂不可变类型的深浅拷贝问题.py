import copy

def test():
    A=[1,2]
    B=[11,22]
    C=(A,B)

    print("A=",A,id(A))
    print("B=",B,id(B))
    print("C=",C,id(C))

    D = copy.copy(C)
    print("D=",D,id(D))
    D[0].append(4)
    print("D[0]=",D[0],id(D[0]))
A=[1,2]
B=[11,22]
C=(A,B)

print("A=",A,id(A))
print("B=",B,id(B))
print("C=",C,id(C))
print("C[0]=",C[0],id(C[0]))

D = copy.deepcopy(C)
print("D=",D,id(D))
D[0].append(4)
print("D[0]=",D[0],id(D[0]))
