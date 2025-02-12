#write a python program for the stactic method
from staticmethod_exp4 import Hyderabad, Student, Teacher


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
        '''
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
ho=hyd()
ho.datainfo(s,"student")
ho.datainfo(e,"employess")
ho.datainfo(t,"teacher")
'''



student = Student()
#student.studval()

#temp = Teacher().teachval()
#print(id(temp))
t=Teacher()
t.teachval()
#print(id(t))
Hyderabad.dispobjdata1(t, "Teacher")
#Hyderabad().dispobjdata(student, "Student")
#wfwgdlfhdslfdslfhdshfgdshfgldshfgsldhflsd




