#write a python python program of the class level data member
#class level data member
class student:
    crs="python"
    city="hyd"
s1=student()
s2=student()
print("-"*50)
print("the content of the s1---{}>".format(len(s1.__dict__)))
print("the course of the student{}".format(student.crs))
print("the studen of the city{}".format(student.city))
print("*"*50)
print("the content of the s1---{}>".format(len(s2.__dict__)))
print("the course of the student{}".format(student.crs))
print("the studen of the city{}".format(student.city))