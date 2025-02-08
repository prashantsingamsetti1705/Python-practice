#write a python program of the intance data member usin the dynamically
class student():pass
#main program
s1=student()
s2=student()
#intance data member
s1.sno=int(input("enter the first student sno:"))
s1.sname=input("enter the student name:")
s1.marks=float(input("enter the student marks:"))
#second students details
s2.sno=int(input("enter the first student sno:"))
s2.sname=input("enter the student name:")
s2.marks=float(input("enter the student marks:"))
print("*"*50)
print("the first student sno{}".format(s1.sno))
print("the first student name:{}".format(s1.sname))
print("the first student marks{}".format(s1.marks))
print("*"*50)
print("the sec student sno{}".format(s2.sno))
print("the sec student name:{}".format(s2.sname))
print("the sec student marks{}".format(s2.marks))
print("*"*50)

