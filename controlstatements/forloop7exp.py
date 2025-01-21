#write program to compute sum of first natural number
#using while loop
n=int(input("enter how many u want to generate :"))
if n==0:
    print("is invalid number ")
print("*"*50)
print("/t natofnum/t nat ssnum/t nat csnum ")
print("-----------------------------")
s,ss,cs=0,0,0
for i in range(1,n+1):
    print("/t {}/t{}/t/{} ".format(i,i**2,i**3))
    s=s+i
    ss=ss+i**2
    cs=cs+i**3
else:
    print("sum of n natural number{},{},{}".format(s,ss,cs))