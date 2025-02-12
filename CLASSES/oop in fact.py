#write a python program of the factorial of the number using the oops concept
import sys
class Students:
    def readvaules(self):
        try:
            self.n=int(input("enter the factorial of the number:"))
        except ValueError:
            print("dont entre the alpha numerics for")
            sys.exit()
        else:
            self.datavalues()
    def datavalues(self):
        if self.n<0:
            print("invalid input please try agin:")
        else:
            s=1
            for i in range(self.n,0,-1):
                s*=i
            else:
                print("{},{}".format(self.n,s))
Students().readvaules()

