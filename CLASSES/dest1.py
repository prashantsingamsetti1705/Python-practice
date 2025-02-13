#program on the dest
#write a python program of the destructor
import sys
import time
class Student:
    def __init__(self,sno,name):
        self.sno=sno
        self.name=name
        print("the sno of the student :{}".format(self.sno))
        print("the student name:{}".format(self.name))
    def __del__(self):
        global totmem
        totmem=sys.getsizeof(self)
        print("nothe memory space of the =",totmem)
#main program
# Student().getstud(10,"pras")
# Student().getstud(100,"anil")
s=Student(100,"anil")
totmem =sys.getsizeof(s)
print("nothe memory space of the =", totmem)
print("the program excution is done")
time.sleep(10)