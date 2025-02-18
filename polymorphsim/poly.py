#write a python program of poly overriden method example
class Univ:
    def getdata(self):
        self.univname = input("Enter the name of the university: ")
        self.uniloc = input("Enter the location of the university: ")
    def getdisp(self):
        print("*" * 50)
        print("The details of the university:")
        print("The name of the university: {}".format(self.univname))
        print("The location of the university: {}".format(self.uniloc))
        print("*" * 50)

class College:
    def getdata(self):
        self.collegename = input("Enter the name of the college: ")
        self.collegeloc = input("Enter the location of the college: ")
    def getdisp(self):
        print("*" * 50)
        print("The details of the college:")
        print("The name of the college: {}".format(self.collegename))
        print("The location of the college: {}".format(self.collegeloc))
        print("*" * 50)

class Student(Univ, College):
    def getdata(self):
        self.studentname = input("Enter the name of the student: ")
        self.studentnumb = input("Enter the number of the student: ")
        super().getdata()
        College.getdata(self)
    def getdisp(self):
        super().getdisp()
        College.getdisp(self)
        print("*" * 50)
        print("The details of the student:")
        print("The name of the student: {}".format(self.studentname))
        print("The student number: {}".format(self.studentnumb))
        print("*" * 50)

# Main program
s = Student()
s.getdata()
s.getdisp()
