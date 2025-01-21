#write a python program to generate sum of  square and cube
# while using while loop
n=int(input("enter a sum of ss,sc of given n natural number"))
if n<=0:
    print("{} is a invalid number")
else:
    print("/tn ant/t/t/t ss /t/t/t sc ")
    i=1
    s=0
    ss=0
    sc=0
    while i<=n:
        print(" {} {} {} ".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        sc=sc+i**3
        i=i+1
    else:
        print("*"*50)
        print(" {} {} {}".format(s,ss,sc))