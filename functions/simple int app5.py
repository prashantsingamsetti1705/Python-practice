#write a python program which will calculate simple int and total input
#simple int
def simplint():
    #taking input fuction inside of the body
    p=float(input("enter value of principle Amount:"))
    t= float(input("enter value of time:"))
    r= float(input("enter value of rate of intrest:"))
    lst=[]
    if p<0:
        lst.append(print("invalid input"))
    if r<0:
        lst.append(print("invalid input"))
    if t<0:
        lst.append(print("invalid input"))
        print(lst)
    if p<=0 or r<=0 or t<=0:
        return"".join(lst)
    else:
        si=p*t*r/100
        tl=p+si
        return p,t,r,si,tl
a,b,c,d,res=simplint()
print("enter the{} {} {} ={}".format(a,b,c,d,res))
