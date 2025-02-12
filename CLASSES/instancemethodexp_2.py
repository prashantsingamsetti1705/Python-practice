#write a python program of the inastance method and instance data memeber creating the the object
from calendar import firstweekday


class employees:
    def reademp(self,obj):
        print("the information {} of the employees".format(obj))
        self.eno=int(input("enter the employeenumber :"))
        self.ename=input("enter the employee name:")
        self.esal=float(input("enter the employee sal:"))
    def dispemp(self,obj):
        print("the information {} of the employees".format(obj))
        print("the eno {} of the employees".format(self.eno))
        print("the ename {} of the employees".format(self.ename))
        print("the esal {} of the employees".format(self.esal))
#instance data member craeting the object
e1=employees()
e2=employees()
print("Content of S1 Object=",e1.__dict__)
print("Content of S2 Object=",e2.__dict__)
e1.reademp("first")
e1.dispemp("first")
print("*"*50)
e2.reademp("first")
e2.dispemp("first")

