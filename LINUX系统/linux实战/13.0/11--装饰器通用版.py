def function_out(func):

    def function_in(num,*args,**kwargs):
        print("-------num-------",num)
        print("-------agrs----",args)
        print("-------kwargs-------",kwargs)

        return func(num,*args,**kwargs)        
    return function_in

@function_out
def login(num,*args,**kwargs):
    print("-------num-------",num)
    print("-------agrs----",args)
    print("-------kwargs-------",kwargs)

    return num 

result = login(10,10,a=10)
print(result)