from divi import div
from excepts import DivisonError
try:
    a=int(input("enter the a value of a"))
    b=int(input("enter a value of b"))
    r=div(a,b) # Function Call---gives the Result OR Exception
except DivisonError:
    print("dont enter the denominator zero u will get the error")
except ValueError:
    print("do not enter alpha num u will get error")
else:
    print("div of value a={}\ndiv of value b={}\nresult of r={}".format(a,b,r))
finally:
    print("iam from the finally")
#Phase-3: Handling the exceptions