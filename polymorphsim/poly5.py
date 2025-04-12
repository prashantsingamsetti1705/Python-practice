#write a python program on polymorphism using the constrcuctor overriden
class Circle:
    def __init__(self):# default constructor method
        print("get the circle")
class Square(Circle):
    def __init__(self):#conrstrctor overridden
        print("get suare")
        super().__init__()
class rect(Square):
    def __init__(self):
        print("get the rect")
        super().__init__()
#main program creating obj
rc=rect()