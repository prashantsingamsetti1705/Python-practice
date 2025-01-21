# Python | Cloning or Copying a list
#logic-1
lst1=[10,20,20,40,50]
lst2=lst1
print(lst2)
# logic-2
n=int(input("enter a numbers u want in a list"))
if n<=0:
    print("{} is a invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter {} value".format(i)))
        lst.append(val)
    else:
        print(lst)
        lst1=lst
        print("{} is copying a list".format(lst1))