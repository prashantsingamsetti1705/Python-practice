#write aprogram of the dest using the del
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
s1=Student(100,"anil")
s2=s1
s3=s1
print("no more excution and mainting the memory sapce no of the s1")
time.sleep(5)
del s1
print("no more excution and mainting the memory sapce no of the s2")
time.sleep(5)
del s2