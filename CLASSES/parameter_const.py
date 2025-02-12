#parameter const
class Employee:
    def __init__(self,x,y):#parameter constructor
        self.a=x
        self.b=y
        print("the value of the x--->{}".format(self.a))
        print("the value of the y----->{}".format(self.b))
#main program
e=Employee(100,200)
e1=Employee(200,500)

