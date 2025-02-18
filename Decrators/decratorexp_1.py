#a decorator is one of the function which will provide addtional functionality to the normal function.
#a decorator always take the normal function as the parameter
#exampleone

def getsquare(hyd):
    def operation():
        n=hyd()
        res=n**2
        return n,res
    return operation

def getval():
    return 5
op=getsquare(getval)
n,r=op()
print("square of the{}={}".format(n,r))
