#here is the program we had the writing thw the code  emp view and view all by emp eno
# program for read the empdata
import pickle
def viewemp():
    empno=int(input("enter the employee number"))
    emplst=[]
    with open("emp.text","rb") as rp:
        while True:
            try:
                record=pickle.load(rp)
                emplst.append(record)
            except EOFError:
                print("-"*100)
                break
            res="not found"
            for rec in emplst:
                if rec[0]==empno:
                    res="found"
                    res1=rec
                    break
        if res =="found":
            print("EMPLOYEE NUMBER:",res1[0])
            print("employee name:",res1[1])
            print("employee salary:",res1[2])
        else:
            print("employee does not exits",empno)
def viewall():
    with open("emp.text","rb") as rp:
        while True:
            try:
                record=pickle.load(rp)
                for val in record:
                    print(val,end="\t\t")
                print()
            except EOFError:
                print("-"*100)
                break


