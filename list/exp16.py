# Python program to find Cumulative sum of a list
n=int(input("enter a numbers u want in a list"))
if n<=0:
    print("{} is a invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter {} value".format(i)))
        lst.append(val)
    else:
        lst2=[]
        y=0
        for i in (lst):
            y=y+i
            lst2.append(y)
        else:
            print(lst)
            print("{}Cumulative sum of a list is  {}".format(lst,lst2))
