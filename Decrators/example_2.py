#write a python program which is uesd to calculate the square of the
#here are the 2nd example of the decoartor types of the decurators
def square(hyd):#--->decorator--->outer function
    def op():
        a=hyd()
        res=a**2
        return a,res
    return op
#inner function
def getval():
    a=int(input("eneter a value "))
    return a
a,r=square(getval)()
print("square of thvalue is{}--->{}".format(a,r))
