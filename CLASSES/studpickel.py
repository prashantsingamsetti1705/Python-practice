# #write a python program of the student of tthe importing the pickel and etc
from student import student
import pickle
class nitstudentpick:
    def setstudent(self):
        sno=int(input("enter the student number:"))
        sname=input("enter the student name:")
        marks=float(input("enter the marks of the students:"))
        return sno,sname,marks
    def getvalues(self):
            with open("student.text","ab") as fp:
                while True:
                    sno,sname,marks=self.setstudent()
                    no=student()
                    no.getstudvalues(sno,sname,marks)
                    pickle.dump(no,fp)
                    print("the record is insert sucess fully")
                    ch=input("do you want insert the record of the data or not (yes/no):")
                    if ch.lower()=="no":
                        print("thanks for using this program")
                        break
no=nitstudentpick()
no.getvalues()

