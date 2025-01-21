#write a program to genrate a even number of n natural number
#using forloop
n=int(input("enter how many number you want to generate a of even number:"))
if n==0:
    print("{}is a invalid number")
else:
    for val in range(2,n+1,2):
           print(val)