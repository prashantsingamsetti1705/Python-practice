#PolyEx12.py
class Circle:
    def __init__(self,r): # Original Parametrized Const
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square:
    def __init__(self,s): # original  Parametrized Const
        self.sa = s**2
        print("Area of Square=", self.sa)
class Rect(Circle,Square):
    def __init__(self,r=None):pass

    def area(self,L,B): # Overridden  Parametrized Const
        self.ra = L*B
        print("Area of Rect=", self.ra)
        print("-------------------------")
        Square.__init__(self,float(input("Enter Side Value:")))
        print("-------------------------")
        Circle.__init__(self,float(input("Enter Radius:")))

#Main Program
r=Rect().area(float(input("enter the lenfth of the rec")),float(input("enter the breath of the rec"))) # Object Creation