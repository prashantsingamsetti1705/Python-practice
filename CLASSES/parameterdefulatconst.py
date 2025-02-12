#defualt,parameter
class Student:
     def __init__(self,a=1,b=2):# Default and Parameterized Constuctor
         self.a=a
         self.b=b
         print("the value of the {}".format(self.a))
         print("the value of the {}".format(self.b))
#mainprogram
s=Student()
s1=Student(10,200)
s2=Student(b=2000,a=200)
