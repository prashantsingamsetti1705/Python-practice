# write a python program which will accept list of values and display only ve+ values:
n=int(input("enter number of values :"))
if n<=0:
    print("{}is is invalid input please enter a +ve".format(n))
else:
    print("--------------------------")
    lst=[]
    print("enter a values in the list")
    for i in range(1,n+1):
        lst.append(float(input("{} enter the value of list".format(i))))
    else:
        print("enter the list values")
        print(lst)
        llst=[]
        for v in lst:
            if v<=0:
                continue
            llst.append(v)
            print("-------------------------")
            print("list of +ve numbers")
            print(llst)

