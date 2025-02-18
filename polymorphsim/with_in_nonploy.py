#write a python program of the non ploymorphsim
#using the instance method
#using the multi level inheritance
class Circle:
    def drawcircle(self):
        print("get the circle")
class Square(Circle):
    def drawsquare(self):
        print("get sqaure")
class Rect(Square):
    def drawrect(self):
        print("get rectangular")
#main program
#creating the object
co=Rect()
print("*"*50)
co.drawcircle()
co.drawsquare()
co.drawrect()
print("*"*50)