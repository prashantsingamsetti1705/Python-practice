#here we are using the oops by using instance Method and connecting the database
import mysql.connector as mysql
class Employeedel:
    def employee_del(self):
        self.eno=int(input("enter the employee eno number:"))
        # self.ename=input("enter the employee ename:")
        # self.esal=float(input("enter the employee sal:"))
        # self.ecompany=input("enter the employee company name:")
    def savedel_data(self):
        try:
            con=mysql.connect(host="localhost",user="root",passwd="1705",database="employee")
            cu=con.cursor()
            iq="delete from employees WHERE eno = %d"
            cu.execute(iq %(self.eno))
            if cu.rowcount<0:
                print("else there is a empty in yor record")
            else:
                con.commit()
                print("the{} record is deleted".format(cu.rowcount))
        except mysql.DatabaseError as db:
            print("there is problem in your db",db)