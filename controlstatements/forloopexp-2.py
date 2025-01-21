#write a program to print a +ve number of nto1
#using while loop
n=int(input("enter how many number u want to genrate:"))
if n<=0:
    print("invalid input")
else:
    for i in range(1,n+1)[::-1] :
        print(i)