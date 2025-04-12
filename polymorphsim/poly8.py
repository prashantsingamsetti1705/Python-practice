class Circle:
    def area(self,r):
        self.tot=3.14*r**2
        print ("the radius of the cricle:{}". format(self.tot))
class Square(Circle):
    def area(self,s):
        self.tot=s**2
        print ("the square:{}". format(self.tot))
        super().area(float(input("eneter the radius of the r:")))
class rec(Square):
    def area(self):
        self.l=float(input("eneter the length of the rec l:"))
        self.b=float(input("eneter the length of the rec b:"))
        self.tot=self.l*self.b
        print ("the area of the rec:{}". format(self.tot))
        super().area(float(input("eneter the side of the square:")))
#main program
roc=rec()
roc.area()