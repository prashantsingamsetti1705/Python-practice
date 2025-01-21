#write a python program to sum
#logic 1
num=int(input("enter any number :"))
if num<=0:
    print("in invalid input={}".format(num))
else:
    ds=0
    for d in str(num):
        ds=ds+int(d)
    else:
        print("sum of digits {}={}".format(num,ds))
#logic 2
num=int(input("enter any number :"))
if num<=0:
    print("in invalid input={}".format(num))
else:
    tn=num
    ds=0
    while num>0:
        d=num%10
        ds=ds+d
        num=num//10
    else:
        print("sum of digits {}={}".format(tn,ds))
