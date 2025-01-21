# Python | Sort the values of first list using second list
#program
n=int(input("enter a numbers u want in a list"))
if n<=0:
    print("{} is a invalid input".format(n))
else:
    lst=[] #empty list
    for i in range(1,n+1):
        val=int(input("enter {} value".format(i)))
        lst.append(val)#apppend value in lst
    else:
        print(lst)
        lst2=[]#empty 2nd list
        for i in range(1,n+1):
            val1=input("{}enter value of second list".format(i))
            lst2.append(val1)#apppend value in list2
        else:
            print(lst2)
            lts3=sorted(zip(lst2,lst))#sorting first list value using second list
            print(lts3)
