#here we are using the oops by using instance Method and connecting the database
import mysql.connector as mysql
class Employeeadd:#instance method
    #adding the emp data
    def employee_add(self):
        self.eno=int(input("enter the employee eno number:"))
        self.ename=input("enter the employee ename:")
        self.esal=float(input("enter the employee sal:"))
        self.ecompany=input("enter the employee company name:")
    def save_data(self):
        try:
            con=mysql.connect(host="localhost",user="root",passwd="1705",database="employee")
            cu=con.cursor()
            iq="insert into employees values(%d,'%s',%f,'%s')"
            cu.execute(iq %(self.eno,self.ename,self.esal,self.ecompany))
            if cu.rowcount<0:
                print("else there is a empty in yor record")
            else:
                con.commit()
                print("the record is insert is {}".format(cu.rowcount))
        except mysql.DatabaseError as db:
            print("this db is already exit please try again",db)

