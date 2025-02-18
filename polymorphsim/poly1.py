#write a python program on the example1 of the ploy
#the proces of the representing one from in multiple forms is called polymorphism
class Circle:
    def draw(self):
        print("get the circle")
class Suqare(Circle):
    def draw(self):#overriden method
        print("get the square")
        super().draw()
class rect(Suqare):
    def draw(self):
        print("get rect")
        super().draw()
#main program
print("wrt rect class")
c2=rect()
c2.draw()