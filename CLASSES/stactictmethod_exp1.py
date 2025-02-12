#program for the static method demonstrating the need of static method
class student:
    def getstudval(slef):
        slef.sno=int(input("enter the student sno"))
        slef.sname=input("enter the student name:")
        slef.marks=float(input("enter the student marks:"))
class employee:
    def getemp(self):
        self.eno=int(input("enter the employee number:"))
        self.ename=input("enter the employee number:")
class teacher:
    def gettech(self):
        self.tno=int(input("enter the teacher number:"))
        self.tname=input("enter the teacher name:")
        self.sub=input("enter the tecaher subject:")
        self.exp=float(input("enter the teacher exp:"))
class hyd:
    @staticmethod
    def dispobjdata(objdata,objinfo):
        print("-"*50)
        print("{}object inormation".format(objinfo))
        print("-"*50)
        for k,v in objdata.__dict__.items():
            print("{}--{}".format(k,v))
        print("-"*50)
#main program,
s=student()
e=employee()
t=teacher()
#read the values for student object
s.getstudval()
#read the value for employess object
e.getemp()
#read the values for teacher employess
t.gettech()
#dispaly the values of any object of annly calss
hyd.dispobjdata(s,"student")
hyd.dispobjdata(e,"employee")
hyd.dispobjdata(t,"teacher")