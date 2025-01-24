import pickle
with open("emp.pick","rb") as fp:
    print("*"*50)
    rd=pickle.load(fp)
    print(rd)
    print("*" * 50)
        # Program for Reading Employee Records from Employee File (emp.pick)
        # EmpUnPickEx1.py
        # import pickle
        #
        # with open("emp.pick", "rb") as fp:
        #     print("----------------------------------")
        #     print("List of Employee Records")
        #     print("----------------------------------")
        #     while (True):
        #         try:
        #             record = pickle.load(fp)
        #             for val in record:
        #                 print(val, end="\t\t")
        #             print()
        #         except EOFError:
        #             print("----------------------------------")
        #             break