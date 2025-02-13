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
# print("the program excution is done")
# time.sleep(5)
# del s1
s2=s1
print("the program excution is done")
time.sleep(10)