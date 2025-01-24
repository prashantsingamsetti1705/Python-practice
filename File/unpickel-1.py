#wite a python program which will read the data the data
import pickle
def upk():
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
#main program
upk()
#Program for Reading Employee Records from Employee File (emp.pick)