#program for demonstating the the class level data member
class student():pass
student.crs="python"
student.city="hyd"#here it is called class level data member
s1=student()
s2=student()
print("*"*50)
print("the length of the content of the s1{}".format(len(s1.__dict__)))
print("the course of the student{}".format(s1.crs))
print("the city of the student{}".format(s2.city))
print("*"*50)
print("the length of the content of the s1{}".format(len(s2.__dict__)))
print("the course of the student{}".format(student.crs))
print("the city of the student{}".format(student.city))
#program for demonstating the the class level data member
class student():pass
student.crs="python"
student.city="hyd"#here it is called class level data member
s1=student()
s2=student()
print("*"*50)
print("the length of the content of the s1{}".format(len(s1.__dict__)))
print("the course of the student{}".format(s2.crs))
print("the city of the student{}".format(s2.city))
print("*"*50)
print("the length of the content of the s1{}".format(len(s2.__dict__)))
print("the course of the student{}".format(student.crs))
print("the city of the student{}".format(student.city))