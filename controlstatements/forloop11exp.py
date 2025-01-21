#write a python program to print a sum of and average
#using while loop
n=int(input("enter a value  sum &and average "))
if n==0:
    print("{}is invalid input".format(n))
else:
    print("/t sum/t average")
    s=0
    for i in range(1,n+1):
        i=float(input("enter a number :".format(i)))
        s=s+i
    else:
        print(" sum of {}".format(s))
        print("average of {}".format(s/n))
