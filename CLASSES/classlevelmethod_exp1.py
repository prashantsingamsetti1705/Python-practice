#wtite a pyhon program of the class level method
class student:
    @classmethod
    def getcrs(cls):
        student.crs="python"
        student.city="hyd"
student.getcrs()
s1=student()
s2=student()
print("the content of the student s1{}".format(s1.__dict__))
print("the content of the student s1{}".format(s2.__dict__))
print("*"*50)
print("the student course=",student.crs)
print("the student course=",student.city)
print("*"*50)
print("the student course=",student.crs)
print("the student course=",student.city)