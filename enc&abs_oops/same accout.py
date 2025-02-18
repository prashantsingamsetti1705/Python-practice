#write a python program of the account handling in the same calss
class Account:
    def __init__(self):
        self.__acno=1705
        self.__acname="subbarao"
        self.__acpin=1463
        self.__acbname="sbi"
        self.__acbal=174440.0
    def getval(self):
        print("the account number is {}".format(self.__acno))
        print("the account name is {}".format(self.__acname))
        print("the account pin is {}".format(self.__acpin))
        print("the account bank name is {}".format(self.__acbname))
        print("the account balance is {}".format(self.__acbal))
ac=Account()#creating the obj
ac.getval()