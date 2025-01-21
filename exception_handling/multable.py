from mulexception import ZeroError,NegError
def table(n):
    if n==0:
        raise ZeroError
    elif n<0:
        raise NegError
    if n>0:
        print("*"*50)
        print("mul of table:{}".format(n))
        for i in range(1,11):
            print("{}*{}={}".format(n,i,n*i))
        print("*"*50)