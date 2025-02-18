#write a python program on the polymorphsim sample exampl2
class Circle:
    def draw(self):
        print("get circle")
class Sqaure(Circle):
    def draw(self):
        print("get sqaure")
class Rec(Sqaure):
    def draw(self):
        print("get rec")
        Sqaure().draw()
        Circle.draw(self)
#main program
print("wrts rec class")
#creating the object
co=Rec()
co.draw()