#write program to generate multiplication of the table
#using while loop
n=int(input("enter how many u want to generate :"))
if n==0:
    print("is invalid number ")
print("*"*50)
print("/t/t is mul tabel")
print("-----------------------------")
for i in range(1,11):
    print("/t {}X{} ={} ".format(i,n,i*n))
