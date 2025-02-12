#write a python program of the constructor
from sys import stdlib_module_names


class Employee:
    def __init__(self):
        print("iam from constructor")
        self.eno=100
        self.ename="prashant"
#main program
eo1=Employee()#object is created --pvm automatically call one special method constructor
print(eo1.__dict__)
eo2=Employee()#object is created --pvm automatically call one special method constructor
print(eo2.__dict__)
