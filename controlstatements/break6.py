n=int(input("enter how many values in list:"))
if n==0:
    print("{} is invalid input plese try again".format(n))
else:
    lst=[]# use empty list which will accept
    for v in range(1,n+1):
        lst.append(float(input("enter {} value:".format(v))))
    else:
        print("given list of elements")
        print(lst)
        plst=[]
        for v in lst:
            plst.append(v*v)
        else:
            print("product list of elements ")
        print(plst)