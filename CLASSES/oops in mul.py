#write a python program of the factorial of table of the number
import sys
class Table:
    def readtabel(self):
        try:
            self.n=int(input("enter the number of mul of the table:"))
            self.getvalues()
        except ValueError:
            print("do not enter alpha nums for the n")
            sys.exit()
    def getvalues(self):
        if self.n<=0:
            print("inavalid input")
        else:
            print("*" * 50)
            print("the mul of the table of {}".format(self.n))
            print("*"*50)
            for i in range(1,11):
                print("{}*{}--->{}".format(self.n,i,self.n*i))
            print("*"*50)
no=Table()
no.readtabel()
# no.getvalues()