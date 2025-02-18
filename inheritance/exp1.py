# Example of program of the single inheritance
class c1:#base class
    def Parent(self):
        print("iam from the parent class")
class c2(c1):#child class
    def Child(self):
        print("iam from the child class")
#main program
#creating the obj1
co2=c2()
co2.Parent()
co2.Child()