#wite a python program which will read the data the data
import pickle
with open("emp.txt","rb") as fp:
    print("-"*50)
    while True:
        try:
            record=pickle.load(fp)
            for val in record:
                print(val,end="\t\t")
            print()
        except EOFError:
            print("-"*50)
            break
#Program for Reading Employee Records from Employee File (emp.pick)
#EmpUnPickEx1.py
# import pickle
# with open("emp.txt","rb") as fp:
#     print("----------------------------------")
#     print("List of Employee Records")
#     print("----------------------------------")
#     while(True):
#         try:
#             record = pickle.load(fp)
#             for val in record:
#                 print(val,end="\t\t")
#             print()
#         except EOFError:
#             print("----------------------------------")
#             break