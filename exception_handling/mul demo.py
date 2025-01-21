from multable import table
from mulexception import ZeroError,NegError
while True:
    try:
        n=int(input("enter a number :"))
        table(n)
    except ZeroError:
        print("dnot enter the zero u will get error")
    except NegError:
        print("dont enter the negtive error")
    except ValueError:
        print("dont enter the alnum")
    except:
        print("opps some thing")
    else:
        ch=input("enter du want another table Yes/no")
        if not ch.isalpha():
            print("enter the dont enter the digit")
        else:
            if ch.lower()=="no":
                print("thanks for using this program")
                break