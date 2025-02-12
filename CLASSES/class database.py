#write a python program of the connection data base  through the class
#
import mysql.connector
class Students:
    def studvalues(self):
        self.sno=int(input("enter the student number:"))
        self.sname=input("enter the student name:")
        self.marks=float(input("enter the marks of the students:"))
    def studdata(self):
        try:
            con=mysql.connector.connect(host="localhost",user="root",passwd="1705",database="student")
            cu=con.cursor()
            iq="insert into students values(%d,'%s',%f)"
            cu.execute(iq%(self.sno,self.sname,self.marks))
            con.commit()
            print("{}record is inserted into the students table".format(cu.rowcount))
        except mysql.connector.DatabaseError as db:
            print("the ther is problem in your db--->",db)
s=Students()
s.studvalues()
s.studdata()