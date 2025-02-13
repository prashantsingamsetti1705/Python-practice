#write a python program of the destructor
class Student:
    def __init__(self,sno,name):
        self.sno=sno
        self.name=name
        print("the sno of the student :{}".format(self.sno))
        print("the student name:{}".format(self.name))
#main program
# Student().getstud(10,"pras")
# Student().getstud(100,"anil")
s=Student(100,"anil")#here gc collects all the objects memory sapce which used in current program and this type of the memory sapce eilamtion of the object is called Automatic gc
#note every gc