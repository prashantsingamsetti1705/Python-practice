#here we are using the oops by using instance Method and connecting the database
import mysql.connector as mysql
class Employeeview:
    def view_employee(self):
        self.eno = int(input("Enter the employee eno number to view: "))
    def view_data(self):
        try:
            con = mysql.connect(host="localhost", user="root", passwd="1705", database="employee")
            cu = con.cursor()
            iq = "SELECT * FROM employees WHERE eno = %s"
            cu.execute(iq, (self.eno,))
            result = cu.fetchone()
            if result:
                print(f"eno: {result[0]}")
                print(f"ename: {result[1]}")
                print(f"esal: {result[2]}")
                print(f"ecompany: {result[3]}")
        except mysql.DatabaseError as db:
            print("there is problem in your db",db)
    def emp_viewall(self):

        try:
            con=mysql.connect(host="localhost",user="root",passwd="1705",database="employee")
            cu=con.cursor()
            iq="select *from employees"
            cu.execute(iq)
            for colname in cu.description:
                print("\t{}".format(colname[0]),end="\t")
            print()
            res=cu.fetchall()
            if cu.rowcount>0:
                # print(res)
                for recored in res:
                    for val in recored:
                        print("\t{}".format(val),end="\t")
                    print()
            else:
                print("No record found with the provided employee number.")
        except mysql.DatabaseError as db:
            print("there is problem in your db",db)