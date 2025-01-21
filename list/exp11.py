# Remove multiple elements from a list in Python
n=int(input("enter a how many number u want:"))
if n<=0:
    print("{}in valid input ".format(n))
else:
    lst=[]
    for i in range (1,n+1):
        val=int(input("enter {} value ".format(i)))
        lst.append(val)
    else:
        print(lst)
        print("inter change of first and kast lst element of list {}".format(lst.remove()))
