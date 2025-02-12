#write a python of the non constructor
class Student():
    def Getsutd(self):#instance method
        self.sno=100
        self.name="prashant"
#mainpeogram
s=Student()
print("the after caling the content of the {}".format(s.__dict__))#we get the ----><empty {}
s.Getsutd()
print("the after caling the content of the {}".format(s.__dict__))

