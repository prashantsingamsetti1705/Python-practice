#write pyhton program to generate a product of natural number
#using while loop
n=int(input("enter how many u want to generate :"))
if n==0:
    print("is invalid number ")
else:
    p=1
    print("*"*50)
    for val in range(1,n+1)[::-1]:
        print(val)
        p=p*val
    else:
        print("the product of n natural number{} ".format(p))
