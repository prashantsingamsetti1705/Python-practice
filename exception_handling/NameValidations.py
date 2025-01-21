from invalidexception import InvalidNameError,SpaceError,ZeroLengthNameError
def validate(name:str): #name=123Guido Van Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split() # words=['123Guido','Van','Rossum']
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return name
        else:
            raise InvalidNameError
