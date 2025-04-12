#write a python program on polymorphism using the constrcuctor overriden
class Circle:
    def area(self,r):#istance method
        self.tot=3.14*r**2
        print ("the radius of the cricle:{}". format(self.tot))
class Square(Circle):
    def area(self,s):
        self.tot=s**2
        print ("the square:{}". format(self.tot))
        super().area(float(input("eneter the radius of the r:")))
class rec(Square):
    def area(self,l,b):
        self.tot=l*b
        print ("the area of the rec:{}". format(self.tot))
        super().area(float(input("eneter the side of the square:")))