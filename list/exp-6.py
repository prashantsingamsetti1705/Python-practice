# Python program to find sum of elements in list
n=int(input("enter a how many number u want:"))
if n<=0:
    print("{} in valid input".format(n))
else:
    lst=[]
    for i in range (1,n+1):
        val=int(input("enter value".format(i)))
        lst.append(val)
    else:
        s=0
        for i in lst:
            s=s+i
        else:
            print("{} is sum of list{}".format(lst,s))
