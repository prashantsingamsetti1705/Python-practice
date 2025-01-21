#here simpleint----> file name --->module name
#write a python program of simple int
bname="HDFC"
addr="ponnur-->Ap"
def simpleint():
    p=float(input("enter the value of principle"))
    t=float(input("enter the value of time"))
    r=float(input("enter the rate of intrest"))
    si=(p*t*r)/100
    totalamount=p+si
    #display result
    print("*"*50)
    print("the principlr amount is={}".format(p))
    print("the time duration is={}".format(t))
    print("the rate of interest amount is={}".format(r))
    print("the simple interest amount is={}".format(si))
    print("the total amount is={}".format(totalamount))
    print("*"*50)