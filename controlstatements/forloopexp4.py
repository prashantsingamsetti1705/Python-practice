#write a program to generate a odd number of n natural number
#using forloop
n=int(input("enter how many number you want to generate a of odd number:"))
if n==0:
    print("{}is a invalid number")
else:
    for val in range(1,n+1,2):
           print(val)