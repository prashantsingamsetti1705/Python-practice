
#write a python program on polymorphism using the constrcuctor overriden
class Circle:#instance method using the parameters
    def __init__(self,r):# default constructor method
        self.tot=3.14*r**2
        print("the radus of the circle{}".format(self.tot))
class Square(Circle):
    def __init__(self,s):# default constructor method
        self.tot=s**2
        print("the side of the square is {}".format(self.tot))
class rect(Square):
    def __init__(self,l,b):# default constructor method
        self.tot=l*b
        print("the lengthe breath of the rec{}".format(self.tot))
        print("-"*50)
        super().__init__(float(input("enter the side of the square")))
        print("-"*50)
        Circle.__init__(self,float(input("enter the radius of the circle")))
#main program creating obj
print("wrt the rec class")
l=float(input("enter the length of the rec"))
b=float(input("enter the breath of the rec"))
rc=rect(l,b)
#write a python program on polymorphism using the constrcuctor overriden
class Circle:#instance method using the parameters
    def __init__(self,r):# default constructor method
        self.tot=3.14*r**2
        print("the radus of the circle{}".format(self.tot))
class Square:
    def __init__(self,s):# default constructor method
        self.tot=s**2
        print("the side of the square is {}".format(self.tot))
class rect(Square,Circle):
    def __init__(self,l,b):# default constructor method
        self.tot=l*b
        print("the lengthe breath of the rec{}".format(self.tot))
        print("-"*50)
        Square.__init__(self,float(input("enter the side of the square")))
        print("-"*50)
        Circle.__init__(self,float(input("enter the radius of the circle")))
#main program creating obj
print("wrt the rec class")
l=float(input("enter the length of the rec"))
b=float(input("enter the breath of the rec"))
rc=rect(l,b)