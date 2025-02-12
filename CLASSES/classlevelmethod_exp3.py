#write a python program of the calss level method
class student():
    @classmethod
    def getcity(cls):
        cls.city="goa"
    @classmethod
    def getcrs(cls):
        cls.crs="python"
    def readvalues(self,obj):
        print("the student inforamtion{}".format(obj))
        self.sno=int(input("\t enter the student eno:"))
        self.sname=input(" \t enter the student name:")
        self.marks=float(input("\t enter the marks of the student:"))
    def dispval(self,obj):
        print("the student inforamtion{}".format(obj))
        print("the student number{}".format(self.sno))
        print("the student name{}".format(self.sname))
        print("the student marks{}".format(self.marks))
#instance data member
s1=student()
s2=student()
student.getcity()
student.getcrs()
print("*"*50)
s1.readvalues("first")
s1.dispval("first")
print("*"*50)
s2.readvalues("second")
s2.dispval("second")