#second approarch
class student:pass
p1=student()
p2=student()
print("the value in the p1--->{}".format(p1.__dict__))
print("the number of the value in the p1---->{}".format(len(p1.__dict__)))
print("the id of the p1--->{}".format(id(p1.__dict__)))
p1.pno=12
p1.pname="prashant"
p1.psal=350000.0
p2.pno=13
p2.pname="anil"
p2.psal=350000.0
print("the number of pno--{}".format(p1.pno))
print("the pname--{}".format(p1.pname))
print("the sal of psal--{}".format(p1.psal))
print("*"*50)
print("the number of pno--{}".format(p2.pno))
print("the pname--{}".format(p2.pname))
print("the sal of psal--{}".format(p2.psal))