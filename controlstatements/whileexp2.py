#write a python program to generate n to 1
# using the while loop
n= int(input("enter value of n:"))
if n<=0:
    print("{} is invalid input ")
else:
    i=1
    while i<=n :
        print(i)
        i=i+1
    else:
        print("is else part of while")
    print("while execution is over ")
print("iam from if else statement")
