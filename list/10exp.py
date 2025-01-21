# Python program to print all positive numbers in a range
n=int(input("enter how number u want"))
if n<=0:
    print("{} is invalid input please try again:")
else:
    for i in range(1,n+1):
        print("{} is postive number".format(i))
# Python program to print all negative numbers in a range
n=int(input("enter how number u want"))
for i in range(-6,-1):
        print("{} is -ve number".format(i))