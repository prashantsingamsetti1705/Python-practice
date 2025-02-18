import mysql.connector as mysql
class EmployeeSearch:
    def search_employee(self):
        self.eno = int(input("Enter the employee eno number to search: "))
    def search_data(self):
        try:
            con = mysql.connect(host="localhost", user="root", passwd="1705", database="employee")
            cu = con.cursor()
            iq = "SELECT * FROM employees WHERE eno = %s"
            cu.execute(iq, (self.eno,))
            result = cu.fetchone()
            if result:
                print("Employee Found:")
                print(f"eno: {result[0]}")
                print(f"ename: {result[1]}")
                print(f"esal: {result[2]}")
                print(f"ecompany: {result[3]}")
            else:
                print("No employee found with that eno.")
        except mysql.DatabaseError as db_error:
            print(f"Database error: {db_error}")

