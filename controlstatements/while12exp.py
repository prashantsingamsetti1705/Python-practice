n=int(input("Enter Number for Cal Factorial:"))
if n<=0:
    print("{} is Invalid Input:".format(n))
else:
    f=1
    i=n
    while i>=1:
        print(i)
        f=f*i
        i=i-1
    else:
        print("-"*50)
        print("Factorial({})={}".format(n,f,))
        print("-" * 50)