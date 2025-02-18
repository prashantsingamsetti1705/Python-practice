#write a python program wchich used to creatae a square of the number and squareroot of number
def squareroot(pras):
    def call():
        n,sqr=pras()
        sqrt=n**0.5
        return n,sqr,sqrt
    return call
def square(hyd):
    def operation():
        n=hyd()
        res=n**2
        return n,res
    return operation
@squareroot
@square
def getval():
    return float(input("enter the number number which you want to genarte a square"))
n,sqr,sqrt=getval()
print("enetrhe suare of the number{}---{}".format(n,sqr))
print("enetrhe suare of the number{}---{}".format(n,sqrt))

