#write apython program to print sum of +ve numerical numbers
n=int(input("enter number of values :"))
if n<=0:
    print("{}is is invalid input please enter a +ve".format(n))
else:
    print("--------------------------")
    lst=[]
    ps=0
    print("enter a values in the list")
    for i in range(1,n+1):
        lst.append(float(input("{} enter the value of list".format(i))))
        ps=ps+1
    else:
        print("enter the list values")
        print("{}is the positive value".format(ps))
        print(lst)
        llst=[]
        ns=0
        for v in lst:
            if v==0:
                continue
            llst.append(v)
            ns=ns+1
            print("-------------------------")
            print("list of +ve numbers")
            print(llst)
            print("{}is the ngeitive value".format(ns))



