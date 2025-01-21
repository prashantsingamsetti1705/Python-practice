#write program to compute sum of first natural number
#using while loop
n=int(input("enter how many u want to generate :"))
if n==0:
    print("is invalid number ")
print("*"*50)
print("/t/t sum of n  natural number ")
print("-----------------------------")

s=0
for i in range(1,n+1):
    print("/t {} ".format(i,))
    s=s+i
else:
    print("sum of n natural number{}".format(s))