# Python | Multiply all numbers in the list
n=int(input("enter a how many number u want:"))
if n<=0:
    print("{} in valid input".format(n))
else:
    lst=[]
    s=1
    for i in range (1,n+1):
        val=int(input("enter value".format(i)))
        lst.append(val)
        s=s*val
    else:
        print("{} malutiple of {}".format(lst,s))





