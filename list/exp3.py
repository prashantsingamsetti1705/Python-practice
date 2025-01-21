# Different ways to clear a list in Python
#remove,clear,pop,del
n=int(input("enter a how many number u want:"))
if n<=0:
    print("{} in valid input".format(n))
else:
    lst=[]
    for i in range (1,n+1):
        val=int(input("enter value".format(i)))
        lst.append(val)
    else:
        print("remove of two element of list {}".format(lst.clear()))

