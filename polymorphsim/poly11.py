#PolyEx17.py
class Circle:
    def __init__(self,r): # Original Parametrized Const
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square:
    def __init__(self,s): # original  Parametrized Const
        self.sa = s**2
        print("Area of Square=", self.sa)
class Rect(Circle,Square):
    def __init__(self,L,B): # Overridden  Parametrized Const
        self.ra = L*B
        print("Area of Rect=", self.ra)
        print("-------------------------")
        Square.__init__(self,float(input("Enter Side Value:")))
        print("-------------------------")
        Circle.__init__(self,float(input("Enter Radius:")))

#Main Program
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r=Rect(L,B) # Object Creation