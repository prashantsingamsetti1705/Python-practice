#write a python program to  ehich will decide given number is palindrome or not
n=int(input("enter a any number :"))
print("given value{}".format(n))
tn=n
rn=0
while n<=0:
    r=n%10
    rn=rn*10+r
    n=n//10
else:
    if tn==rn:
        print("is palindrome:".format(tn))
    else:
        print("it is not a palindrome:".format(tn))
#