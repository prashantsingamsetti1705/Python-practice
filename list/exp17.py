# Python | Sum of number digits in List
# program
n=int(input("enter a numbers u want in a list"))
if n<=0:
    print("{} is a invalid input".format(n))
else:
    lst=[]#taking an empty list
    for i in range(1,n+1):
        val=input("enter {} value".format(i))
        lst.append(val)
    else:
        lst2=[]#lst2 for adding sum of number digits in list
        for num in lst:#using for loop in forloop
            y=0
            for digits in str(num):
                y=y+int(digits)
            lst2.append(y)
        else:
            print(lst)#digit of list
            print("Sum of number digits in List".format(lst2))