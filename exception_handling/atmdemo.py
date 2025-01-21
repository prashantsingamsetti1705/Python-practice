#here the atmdemo is the opeerformance importing all defmenu and atmexception ,function call
from atmexception import InsuficentfundError,DepositeError,WithdrawError
from atmoperation import dep,watm,balenq
from atmmenu import menu
while True:
    menu()
    try:
        ch=int(input("enter your choice :"))
        match(ch):
            case 1:
                try:
                    dep()
                except ValueError:
                    print("do not enter the alpha numerics u will get the error")
                except DepositeError:
                    print("do no enter the negitive value u will get the error")
            case 2:
                try:
                    watm()
                except ValueError:
                    print("do not enter the alpha numerics u will get the error")
                except WithdrawError:
                    print("do not enter the negitive values u will get the error")
                except InsuficentfundError:
                    print("you no having insuficent funds your not able withdraw")
            case 3:
                balenq()
            case 4:
                print("thanks for using this program")
                break
            case _:
                print("you had choose the wrong operation please try again")
    except ValueError:
        print("soory dont enter the alpha numerics")
