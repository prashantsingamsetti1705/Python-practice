#write a pyton program of the instance method of containg the instance data memeber and class level data member
##instance method
class student:
    def redstudentdata(self,objinfo):
        print("eneter the sudent information {}of the data".format(objinfo))
        self.sno=int(input("enter the student number :"))
        self.sname=input("enter the student name:")
        self.smarks=float(input("enter the student marks:"))
    def dispdata(self,objinfo):
        print("eneter the sudent information {}of the data".format(objinfo))
        print("the student eno is {}".format(self.sno))
        print("the student name is {}".format(self.sname))
        print("the student marks is {}".format(self.smarks))
    #instance data member are  creating the object
s1=student()
s2=student()
print("the content of the obj{}".format(s1.__dict__))
print("the content of the obj{}".format(s2.__dict__))
print("*"*50)
s1.redstudentdata("first")
print("*"*50)
s2.redstudentdata("second")
print("*"*50)
s1.dispdata("first")
print("*"*50)
s2.dispdata("second")