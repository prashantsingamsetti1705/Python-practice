#program on the dest
#write a python program of the destructor
import sys
import time
class Student:
    def __init__(self,sno,name):
        print("the id of the self:{}".format(id(self)))
        self.sno=sno
        self.name=name
        print("the sno of the student :{}".format(self.sno))
        print("the student name:{}".format(self.name))
    def __del__(self):
        print("the id of the self:{}".format(id(self)))
#main program
# Student().getstud(10,"pras")
# Student().getstud(100,"anil")
s=Student(100,"anil")
print("the program excution is done")
time.sleep(10)