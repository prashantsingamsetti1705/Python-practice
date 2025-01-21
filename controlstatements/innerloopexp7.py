#write a python program which will aceept the list of numerical value and genrate there multiplication
n=int(input("enter how many number you want to prime nuber:"))
if n<=0:
    print("invalid input{}".format(n))
else:
    print("*"*50)
    lst=[]
    for i in range(1,n+1):
        lst.append(int(input("{}number of value in a list".format(i))))
    else:
        print(lst)
        lst2=[]
        for value in lst:
            if value<=1:
                continue
            res=True
            for i in range(2,value):
                if value %i==0:
                    res=False
                    break
            if res:
                lst2.append(value)
        print("{}".format(lst2))



