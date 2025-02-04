#EmpUpdate.py<----File Name and Module Name
import pickle
def updateemp():
    with open("emp.text","rb") as fp:
        # get Employee Number to delete the record
        empno = int(input("Enter Employee Number to update emp name and sal:"))
        empname=input("Enter Ur Correct Name:")
        empsal=float(input("Enter Ur New Salary:"))
        #get the records from file
        emplist = []
        while (True):
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
    res=False
    for ind in range(len(emplist)):
        if(emplist[ind][0]==empno):
            index = ind
            res = True
            break
    if(res):
        emplist[index][1]=empname
        emplist[index][2]=empsal
        print("Employee Data Updated-Verify")
        with open("employee.data","wb") as fp:
            for record in emplist:
                pickle.dump(record,fp)
        print("\tEmployee Data Updated-Verify")
    else:
        print("\tEmployee number does not exist-can't update")