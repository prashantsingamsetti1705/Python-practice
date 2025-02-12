#const example 2
class Student:
    def __init__(self,sno,name):#parameterized contstructor
        print("iam from the constructor")
        self.sno=sno
        self.name=name
#main program
so=Student(100,"prasahnt")#here when object is created --pvm automatically call one special method consturctor
print(so.__dict__)
so1=Student(200,"anil")
print(so1.__dict__)