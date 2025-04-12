
#write a python program on polymorphism using the constrcuctor overriden
class Circle:#instance method using the parameters
    def area(self):# default constructor method
        self.r=float(input("enter thye radius of the r:"))
        self.to=3.14*self.r**2
        print("the radus of the circle{}".format(self.to))
class Square(Circle):
    def area(self):# default constructor method
        self.s=float(input("enter thye radius of the s:"))
        self.to=self.s**2
        print("the side of the square is {}".format(self.to))
        super().area()
class rect(Square):
    def area(self):# default constructor method
        self.l=float(input("enter the length of the rec:"))
        self.b=float(input("enter the breath of the rec :"))
        self.to=self.l*self.b
        print("the lengthe breath of the rec{}".format(self.to))
        super().area()
#main program creating obj
print("wrt the rec class")
rc=rect()
rc.area()
print("*"*50)