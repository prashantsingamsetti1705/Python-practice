#write a python program wchich is used to genrate the cube,suare,squareroot
def cube(sai):
    def cubecal():
        n,sqr,sqrt=sai()
        cub=n**3
        return n,sqr,sqrt,cub
    return cubecal
def squareroot(prash):
    def sqrtcal():
        n,sqr=prash()
        sqrt=n**0.5
        return n,sqr,sqrt
    return sqrtcal
def square(hyd):
    def operation():
        n=hyd()
        res=n**2
        return n,res
    return operation
@cube
@squareroot
@square
def getval():
    return float(input("eneter a number"))
n,sqr,sqrt,cub=getval()
print("enetr the square of the number---{}--{}".format(n,sqr))
print("enter the squareroot of the number---{}---{}".format(n,sqrt))
print("enter the cube of the number is ---{}---{}".format(n,cub))
