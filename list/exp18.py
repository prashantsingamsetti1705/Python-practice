# Break a list into chunks of size N in Python
l=[1,2,3,4,5,6,7,8,9,10]
n=3 #size of chunks
s=[l[i:i+n] for i in range(0,len(l),n)]
print(s)
# program
n=int(input("enter a numbers u want in a list"))
if n<=0:
    print("{} is a invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter {} value".format(i)))
        lst.append(val)#add value in list
    else:
        print(lst)
        l=3
        s=[lst[i:i+l] for i in range(0,len(lst),l)]#here lst[i:i+l]slicing the list
        print("list into chunks of size n in pyhton{}".format(s))