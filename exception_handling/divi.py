from excepts import DivisonError
def div(a,b):
    if b==0:
        raise DivisonError # Hitting the Programmer-Defined Exception
    else:
        return a/b
    # Phase-2: Hiting the Programmer Exceptions