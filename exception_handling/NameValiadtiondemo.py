from invalidexception import InvalidNameError,SpaceError,ZeroLengthNameError
from NameValidations import validate
try:
    name=input("enter you name:")
    res=validate(name)
except InvalidNameError:
    print("is invalid name")
except ZeroLengthNameError :
    print("try enter your name")
except SpaceError:
    print("don't enter the space")
else:
    print("valid name=",res)