#write a python program given number is prime or not
from traceback import print_exc

n=int(input("enter a number :"))
if n<=1:
    print("{} is a in valid number".format(n))
else:
    res="prime"
    for i in range(2,n):
        if n%i==0:
            res="not prime"
            break
    print("{}is {}".format(n,res))
n=int(input("enter a number :"))
if n<=1:
    print("{} is a in valid number".format(n))
else:
    res=True
    for i in range(2,n):
        if n%i==0:
            res=False
            break
    print("{}is prime".format(n) if res else "{}is not prime".format(n))

