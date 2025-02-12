#denomesattring the stactuc method of the data
class Student:
    def studval(self): # instance method
        self.sno=int(input("enter the student number:"))
        self.name=input("enter the student name:")
        self.marks=float(input("enter the student marks:"))

class Employee:
    def empval(self): # instance method
        self.eno=int(input("enter the employee number:"))
        self.name=input("enter the employee name:")
        self.sal=float(input("enter the employee sal:"))

class Teacher:
    def teachval(self): # instance method
        self.tno=int(input("enter the teacher number:"))
        self.tname=input("enter the student teacher name:")
        self.exp=float(input("enter the teacher exp:"))

class Hyderabad:
    @classmethod
    def dispobjdata1(cls,objdata,objinfo): # class level method
        Hyderabad().dispobjdata2(objdata,objinfo)

    def dispobjdata2(self,objdata,objinfo): # instance method
        self.dispobjdata(objdata,objinfo)

    @staticmethod
    def dispobjdata(objdata,objinfo):# static method
        print("*"*50)
        print("the {} obj data".format(objinfo))
        for k,v in objdata.__dict__.items():
            print("{}--->{}".format(k,v))
        print("*"*50)

'''
s=Student()
e=Employee()
t=Teacher()

s.studval()
e.empval()
t.teachval()

hyd=Hyderabad()
hyd.dispobjdata1(s,"stdent")
hyd.dispobjdata1(e,"employee")
hyd.dispobjdata1(t,"teacher")
'''
