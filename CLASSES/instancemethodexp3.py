#write apython program of the students reading the data
class students:
    def readstd(self,obj):
        print("the inforamtion {} of the student".format(obj))
        self.sno=int(input("enter the student sno:"))
        self.sname=input("enter the student sname:")
        self.smarks=float(input("enter the student marks smarks:"))
        self.dispval(obj)
    def dispval(self,obj):
        print("the inforamtion {} of the student".format(obj))
        print("the student number{}".format(self.sno))
        print("the student name{}".format(self.sname))
        print("the student marks{}".format(self.smarks))
#instance member creating the obj
s1=students()
s2=students()
print("Content of S1 Object=",s1.__dict__)
print("Content of S2 Object=",s2.__dict__)
s1.readstd("frist")
print("*"*50)
s2.readstd("second")
print("*"*50)
