#write a python program on polymorphism using the constrcuctor overriden
class Circle:
    def __init__(self):# default constructor method
        print("get the circle")
class Square:
    def __init__(self):#conrstrctor overridden
        print("get suare")
class rect(Square,Circle):
    def __init__(self):
        print("get the rect")
        super().__init__()
        Circle.__init__(self)
#main program creating obj
rc=rect()

