#write a python program which will accept value and get it reverse order:
#logic1
val=input("enter any value:")
print("given value{}".format(val))
reval=val[::-1]
print("reversed val={}".format(reval))
#logic2
val=input("enter any value:")
print("given value{}".format(val))
reval=" "
for v in val[::-1]:
    reval=reval+v
else:
    print("reversed val={}".format(reval))
#logic 3
n=int(input("enter any value"))
print("given value{}".format(n))
rn=0
while n<0:
    r=n%10
    rn=rn*10+r
    n=n//10
else:
    print("is reversed={}".format(rn))
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