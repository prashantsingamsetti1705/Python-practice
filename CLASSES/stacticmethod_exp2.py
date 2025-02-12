#write a python program for the stactic method
class student:
    def getstud(self):
        self.sno=int(input("enter the student sno:"))
class employess:
    def getempval(self):
        self.eno=int(input("enter the employee number eno:"))
        self.ename=input("enter the student name:")
class teacher:
    def getteach(self):
        self.tno=int(input("enter the teacher number:"))
        self.tname=input("enter the teacher name:")
class hyd:
    @staticmethod
    def datainfo(objdata,objinfo):
        print("*"*50)
        print("the object data{}".format(objinfo))
        print("*" * 50)
        for key,values in objdata.__dict__.items():
            print("{}---->{}".format(key,values))
        print("*"*50)
#mainprogram
s=student()
e=employess()
t=teacher()
#reading the student values
s.getstud()
#reading the empolyess values
e.getempval()
#reading the teacher values
t.getteach()
hyd().datainfo(s,"student")
hyd().datainfo(e,"employess")
hyd().datainfo(t,"teacher")