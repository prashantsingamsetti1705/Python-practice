#write a python program
n=int(input("enter  a +ve number"))
if n<=0:
    print("invalid input")
else:
    i=1
    while i<=n:
        print(i)
        i=i+1
    else:
        print("iam from inner of while")
    print("iam from outer while loop")
print("iam from if else")