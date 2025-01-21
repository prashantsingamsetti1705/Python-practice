#write a python program which will calculate the simple int and total amount
# principle amount,time,rate of the int
#simpl int
def simple_int():
    p=float(input("enter the principle amount:"))
    r=float(input("enter the rate of intrest:"))
    t=float(input("enter time:"))
    if p<=0 or r<=0 or t<=0:
        return "invalid input"
    else:
        si=(p*r*t)
        tl=p+si
        return p,r,t,si,tl
#main program:
res=simple_int()
if type(res)==str:
    print(res)
else:
    #display the result
    print("simple int calculation")
    print("principle amount{}:".format(res[0]))
    print("time :{} ".format(res[2]))
    print("rate of interest:{}".format(res[1]))
    print("simple int {}".format(res[3]))
    print("simple total amount{}".format(res[4]))