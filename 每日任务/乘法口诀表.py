import os
def chengfa():
    for i in range(1,10):
        for j in range(1,i+1):
            #print默认会换行，如果不希望换行则后面加上 end=''，表示以''结束而不是换行符
            print(j,"*",i,"=",j*i,end="  ")
        print("")
            
chengfa()      
    
