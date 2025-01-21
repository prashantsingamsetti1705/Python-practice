from loginException import UserLoginError,PasswordloginError
from loginvaliadation import validation
while True:
    try:
        user=input("enter the username")
        password=input("enter ur password")
        validation(user,password)
    except UserLoginError:
        print("invalid username")
    except PasswordloginError:
        print("inavlid password")
    else:
        ch=input("enter your u want anthoer user(Yes/no)")
        if ch.lower()=="no":
            print("thanks for suing this program")
            break
