#empmain

from menu import Employeemenu
from empadd import Employeeadd
from empupdate import Employeeupdate
from empdelete import Employeedel
from empview import Employeeview
from empsearch import EmployeeSearch
while True:
    try:
        s1=Employeemenu()
        s1.menu()
        ch=int(input("Enter ur choice :"))
        match(ch):
            case 1:
                e1=Employeeadd()#here creating the obj and calling the class
                e1.employee_add()
                e1.save_data()
            case 2:
                e1=Employeedel()
                e1.employee_del()
                e1.savedel_data()
            case 3:
                e1=Employeeupdate()
                e1.employee_update()
                e1.save_updata()
            case 4:
                e1=Employeeview()
                e1.view_employee()
                e1.view_data()
            case 5:
                e1 = Employeeview()
                e1.emp_viewall()

            case 6:
                e1=EmployeeSearch()
                e1.search_employee()
                e1.search_data()
            case 7:
                print("Thank's for using this program")
                break
            case _:
                print("\t ur selection is wrong please try again")
    except ValueError:
        print("\t dont enter alphanum,str and symbols for choice-try again")
