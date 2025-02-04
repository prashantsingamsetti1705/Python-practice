#EmpDelete.py
import pickle
def deleteemp():
    with open("emp.text","rb") as fp:
        try:
            emno=int(input("Enter Employee Number:"))
            emplist=[]
            while(True):
                try:
                    record=pickle.load(fp)
                    emplist.append(record)
                except EOFError:
                    break
            res=False
            for ind,record in enumerate(emplist):
                if(record[0]==emno):
                    index=ind
                    res=True
            if(res):
                emplist.pop(index)
                with open("emp.text", "wb") as fp:
                    for record in emplist:
                        pickle.dump(record, fp)
                print("\tEmployee data Delete successfully.")
            else:
                print("\tEmployee number does not exist-can't Delete")
        except ValueError:
            print("\tDon't enter alnums,strs and symbols for Choice-try again")


