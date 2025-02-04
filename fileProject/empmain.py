#here the main program
from empmenu import menu
from empadd import addEmp
from empdelete import deleteemp
from empsearch import searchemp
from empview import viewall,viewemp
try:
    menu()
    while True:
        ch=int(input("Enter Your Choice"))
        match ch:
            case 1:
                addEmp()
            case 2:
                deleteemp()
            case 3:pass
            case 4:
                viewemp()
            case 5:
                viewall()
            case 6:
                searchemp()
            case 7:
                print("THANKS FOR USING THIS PROGRAM")
                break
            case _:
                print("you had choice wrong option please try again")
except ValueError:
    print("\t do not enter alpha numerics,str and symbols for choice-try again")




