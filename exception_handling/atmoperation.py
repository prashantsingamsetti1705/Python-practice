#here the atm operation his the main program of the program
from atmexception import DepositeError,InsuficentfundError,WithdrawError
bal=500.0
def dep():
    datm=float(input("enter the the deposite ammount:"))
    if datm<=0:
        raise DepositeError
    else:
        global bal
        bal=bal+datm
        print("enter your bank account number 122XXXXXXXXXX:{}".format(datm))
        print("the amount of deposite amount{}".format(bal))
def watm():
    global bal
    watms=float(input("enter the amount how much u want withdraw:"))
    if watms<=0:
        raise WithdrawError
    elif (watms+500)>bal:
        raise InsuficentfundError
    else:
        bal=bal-watms
        print("the your bank account number 122XXXXXXXXXX:{}".format(watms))
        print("the amount of bebit amount of your account inr 122XXXXXXXXXX {}".format(bal))

def balenq():
    print("the avilable balne in your inr 1223XXXXXX account is{}".format(bal))
