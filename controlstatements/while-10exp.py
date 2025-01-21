#write a python program to generate product of a number
# while using while loop
n=int(input("enter a product of a natural number:"))
if n<=0:
    print("{} is a invalid input" )
else:
    print("*"*0)
    i=1
    p=1
    while i<=n:
        print(i)
        p=p*i
        i=i+1
    else:
        print("  a product{}".format(p))
print("this program is completed")