#write a python program on the univercity and collge and student deatils and etc
#write a python program on the univercity and collge and student deatils and etc
class Unvi:
    def getuniv(self):
        self.univname=input("enter the name of the uni:")
        self.univloc=input("enter the name of the location of the uni:")
    def disp(self):
        print("*"*50)
        print("\t univ details")
        print("the univercity name is--{}".format(self.univname))
        print("the univercity loc is{}".format(self.univloc))
        print("*"*50)
class college(Unvi):
    def getcollege(self):
        self.collegename=input("enter the name of the college:")
        self.collegeloc=input("enter the location of the college:")
    def disp1(self):
        print("*"*50)
        print("\t collge details")
        print("the college name is--{}".format(self.collegename))
        print("the college loc is{}".format(self.collegeloc))
        print("*"*50)
class Student(college):
    def getstud(self):
        self.studnumber=int(input("enter the student number:"))
        self.studname=input("enter the student name:")
    def disp2(self):
        print("*"*50)
        print("\t student details")
        print("the univercity name is--{}".format(self.studnumber))
        print("the univercity loc is{}".format(self.studname))
        print("*"*50)
#mainprogram
co3=Student()
co3.getuniv()
co3.getcollege()
co3.getstud()
co3.disp()
co3.disp1()
co3.disp2()
#eample2
class Unvi:
    def getuniv(self):
        self.univname=input("enter the name of the uni:")
        self.univloc=input("enter the name of the location of the uni:")
class college(Unvi):
    def getcollege(self):
        self.collegename=input("enter the name of the college:")
        self.collegeloc=input("enter the location of the college:")
class Student(college):
    def getstud(self):
        self.studnumber=int(input("enter the student number:"))
        self.studname=input("enter the student name:")
    def disp(self):
        print("*"*50)
        print("\t univ details")
        print("the univercity name is--{}".format(self.univname))
        print("the univercity loc is{}".format(self.univloc))
        print("*"*50)
        print("*"*50)
        print("\t collge details")
        print("the univercity name is--{}".format(self.collegename))
        print("the univercity loc is{}".format(self.collegeloc))
        print("*"*50)
        print("*"*50)
        print("\t student details")
        print("the univercity name is--{}".format(self.studnumber))
        print("the univercity loc is{}".format(self.studname))
        print("*"*50)
#mainprogram
co3=Student()
co3.getuniv()
co3.getcollege()
co3.getstud()
co3.disp()

