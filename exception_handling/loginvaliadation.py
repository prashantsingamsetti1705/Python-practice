from loginException import UserLoginError,PasswordloginError
def welcome(user):
    print("it sounda good rembering youe password")
def validation(user,password):
    username=["prasahnt","pinky"]
    passwords=["setti","setty"]
    if user not in username:
        raise UserLoginError
    elif password not in passwords:
        raise PasswordloginError
    else:
        welcome(user)