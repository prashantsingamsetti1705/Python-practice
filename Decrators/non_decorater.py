#write a python which using the with out decorater
def getval():
    return 5
def square():
    n=getval()
    sv=n**2
    print("suare {}---{}".format(n,sv))
def sqrt():
    n=getval()
    sqrt=n**0.5
    print("suare of the {}----{}".format(n,sqrt))
def cube():
    n=getval()
    cub=n**3
    print("the cube of the value{}---{}".format(n,cub))
getval()
square()
sqrt()
cube()
