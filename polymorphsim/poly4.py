#write a python program of poly overriden method example
class univ:
    def getdata(self):
        self.univname=input("enter the name of the university:")
        self.uniloc=input("enter the loc of the univercity")
    def getdisp(self):
        print("*"*50)
        print("the details of the university")
        print("the name of the university{}".format(self.univname))
        print("the loc of the university{}".format(self.uniloc))
        print("*"*50)
class college(univ):
    def getdata(self):
        self.collgename=input("center the name of the college:")
        self.collegeloc=input("enter the loc of the college")
        super().getdata()
    def getdisp(self):
        print("*"*50)
        print("the details of the college")
        print("the name of the college{}".format(self.collgename))
        print("the loc of the college{}".format(self.collegeloc))
        print("*"*50)
        super().getdisp()
class student(college):
    def getdata(self):
        self.studentname=input("center the name of the student:")
        self.studentnumb=input("enter the number of the student:")
        super().getdata()
    def getdisp(self):
        print("*"*50)
        print("the details of the student")
        print("the name of the student{}".format(self.studentname))
        print("the student number{}".format(self.studentnumb))
        print("*"*50)
        super().getdisp()
#main program
co2=student()
co2.getdata()
co2.getdisp()

