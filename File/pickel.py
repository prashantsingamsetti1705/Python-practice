# Program for Reading Employee Deatils and save then File by using Pickling Concpt
# EmpPickEx1.py
import pickle
while True:
    with open("emp.txt","ab") as fp:
        print("*"*50)
        #here empoplye deatails
        eno=int(input("enter the emp number:"))
        en=input("enter the emp name:")
        es=float(input("enter the emp salary:"))
        ed=input("enter the emp disignation:")
        # create an empty list and the place the above values
        lst=[]
        lst.append(eno)
        lst.append(en)
        lst.append(es)
        lst.append(ed)
        pickle.dump(lst,fp)
        print("*"*50)
        print("file saved sucessfully")
        ch=input("du want to enter the the empa data:")
        if ch=="no":
            print("thanks for using this program")
            break
