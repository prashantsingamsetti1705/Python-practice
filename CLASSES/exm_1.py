#write a python program of define of the class
#classes-->class is a collection of the data members and method(function in oops are called methods)
#when we define the class it will not take memeory sapce but-->the data members and the method it will careted a sapce when we create object.
#the programer can store the the the data in data member of object to perform the  operation on data member object using method
#intance data member
class student:pass#--->
s1=student()
s2=student()
print("*"*50)
print("the student sno{}:".format(s1.__dict__))
print("the number of values in s1-->{}".format(len(s1.__dict__)))
print("the the id os the s1--->{}".format(id(s1.__dict__)))#----> here the id will be change
s1.sno=100
s1.sname="prasahnt"
s1.smarks=100
s1.sub="vilisi"
s2.sno=101
s2.sname="anil"
s2.smarks=100
s2.sub="vilisi"
print("*"*50)
print("the student sno{}:".format(s1.__dict__))
print("the number of values in s1-->{}".format(len(s1.__dict__)))
print("the the id os the s1--->{}".format(id(s1.__dict__)))#----> here the id is the different
print("*"*50)
print("the student sno{}:".format(s2.__dict__))
print("the number of values in s2-->{}".format(len(s2.__dict__)))
print("the the id os the s2--->{}".format(id(s2.__dict__)))#----> here the id is the different