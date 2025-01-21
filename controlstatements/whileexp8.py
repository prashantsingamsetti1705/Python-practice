n=int(input("enter number you want to sum"))
if n<=0:
    print("{} is in valid input",format(n))
else:
    print("*"*50)
    i=1
    s=0
    while i<=n:
        print(i)
        s=s+i
        i=i+1
    else:
        print("{} is sum".format(s))


