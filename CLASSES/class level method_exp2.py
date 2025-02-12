#write a python program of the class lvel method
from traceback import print_tb


class empo:
    @classmethod
    def readval(cls):
        cls.city="hyd"
        cls.company="tcs"
        cls.getdeg()
    @classmethod
    def getdeg(cls):
        cls.deg="dev"
empo.readval()
#instance data member creating the object
e1=empo()
e2=empo()
print("*"*50)
print("the coontent of the e1{}".format(e1.__dict__))
print("the coontent of the e2{}".format(e2.__dict__))
print("*"*50)
print("the city of the emp{}".format(e1.city))
print("the city of the emp{}".format(e1.deg))
print("the city of the emp{}".format(e1.company))
print("or")
print("the city of the emp{}".format(empo.city))
print("the city of the emp{}".format(empo.deg))
print("the city of the emp{}".format(empo.company))

#Program for Demonstrating the Class Level Data Members
#ClassLevelMethodEx2.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON" #OR Student.crs="PYTHON"
        #Here crs called Class Level Data Member
        cls.getcity() # calling Class Level Method w.r.t cls
    @classmethod
    def getcity(cls):
        cls.city="HYD" # OR Student.city="HYD"
        # here city is called Class Level Data Member

#Main Program
#Call Class Level Method w.r.t Class Name
Student.getcrs() # calling Class Level Method w.r.t Class name
#Create Objects
s1=Student()
s2=Student()
print("------------------------------------")
print("content of s1=",s1.__dict__)
print("content of s2=",s2.__dict__)
print("------------------------------------")
print("Student Course=",Student.crs)
print("Student City=",Student.city)
print("---------------OR---------------------")
print("Student Course=",s2.crs)
print("Student City=",s2.city)
print("---------------OR---------------------")
print("Student Course=",s1.crs)
print("Student City=",s1.city)

