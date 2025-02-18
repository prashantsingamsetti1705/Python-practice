#write a python program on the polymorphsim sample exampl2
#the proces of the retrieving one from to multiple from is called polymorphism
class Circle:
    def draw(self):
        print("get circle")
class Sqaure:
    def draw(self):
        print("get sqaure")
class Rec(Sqaure,Circle):
    def draw(self):
        print("get rec")
        super().draw()
        Circle.draw(self)
#main program
print("wrts rec class")
#creating the object
co=Rec()
co.draw()