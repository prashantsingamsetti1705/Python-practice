# Python | Remove empty tuples from a list
lst=[10,20,30,(),10]
print(lst.remove(()))
print(lst)
# Python | Program to print duplicates from a list of integers
n=int(input("enter how many numbers u want: "))
if n<=0:
    print("{} is a inavalid number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter a number in a list:".format(i)))
        lst.append(val)
    else:
        print(lst)
        lst2=[]
        t1=set()
        for num in lst:
            if num in t1:
                if num not in lst2:
                    lst2.append(num)
            else:
                t1.add(num)
        print(lst2)
        print(t1)


# n=int(input("enter a numbers u want in a list"))
# if n<=0:
#     print("{} is a invalid input".format(n))
# else:
#     lst=[]
#     for i in range(1,n+1):
#         val=int(input("enter {} value".format(i)))
#         lst.append(val)
#     else:
#         print(lst)
#         lst1=lst
#         print(lst.sort(reverse=False))
#         lst2=lst
#         print(lst2)


