#write a python program of the intance data member usin the dynamically
class student():pass
student.crs="python"
student.city="hyd"#here city,crs are the class level data member
#main program
s1=student()
s2=student()
#palce instance data member object using s1
#intance data member
s1.sno=int(input("enter the first student sno:"))
s1.sname=input("enter the student name:")
s1.marks=float(input("enter the student marks:"))
#palce instance data member object using s1
s2.sno=int(input("enter the first student sno:"))
s2.sname=input("enter the student name:")
s2.marks=float(input("enter the student marks:"))
print("*"*50)
print("the first student sno{}".format(s1.sno))
print("the first student name:{}".format(s1.sname))
print("the first student marks{}".format(s1.marks))
print("the first student course{}".format(student.crs))
print("the first student city{}".format(student.city))
print("*"*50)
print("the sec student sno{}".format(s2.sno))
print("the sec student name:{}".format(s2.sname))
print("the sec student marks{}".format(s2.marks))
print("the first student city{}".format(student.city))
print("the first student course{}".format(student.crs))
print("*"*50)