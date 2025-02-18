#write python program of the multilevel inheritance example
class grandparent:#single class
    def disp1(self):
        print("iam from the grand parent")
class Parent(grandparent):#subclass
    def disp2(self):#base class
        print("iam from the parent calss")
class Child(Parent):
    def disp(self):
        print("ia, from the child class ")

#main program
co3=Child()
co3.disp1()
co3.disp2()
co3.disp()
#example 2
#write python program of the multilevel inheritance example
class grandparent:#single class
    def disp1(self):
        print("iam from the grand parent")
class Parent:#subclass
    def disp2(self):#base class
        print("iam from the parent calss")
class Child(grandparent,Parent):
    def disp(self):
        print("iam, from the child class ")

#main program
co3=Child()
co3.disp1()
co3.disp2()
co3.disp()
