import copy
def test():
    tuple1 = (1,2,3)
    print("tuple1 = ",tuple1,id(tuple1))


    tuple2 = copy.copy(tuple1)

    print("tuple2=",tuple2,id(tuple2))

tuple1 = (1,2,3)
print("tuple1 = ",tuple1,id(tuple1))


tuple2 = copy.deepcopy(tuple1)

print("tuple2=",tuple2,id(tuple2))