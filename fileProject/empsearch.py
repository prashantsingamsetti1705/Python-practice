#EmpSearch.py<----File Name and module name
import pickle
def searchemp():
    # get employee number from KBD
    empno = int(input(("Enter Employee Number:")))
    # Get the Data from the File
    emplist = []
    with open("emp.text", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
        res = "NotFound"
        for emprec in emplist:
            if (emprec[0] == empno):
                res = "found"
                break
        if (res == "found"):
            print("\t{} Employee Number  Exist".format(empno))
        else:
            print("\t{} Employee Number Does not Exist".format(empno))