# write a python program to which will generate odd number with  in n
#using while loop
n=input("enter a value of n generate of odd number: ")
n=int(n)
if n<=0:
    print("{}is a invalid input".format (n))
else:
    i=1
    while i<=n:
        print(i)
        i=i+2
    else:
        print("*"*50)
print("this is invalid input ",format(n))
