#write python program of the single inheritance reading the  value by dinamically
class parent:
    def disp(self):
        self.pprop=float(input("enter the parent prop value:"))
class child(parent):
    def disp1(self):
        self.disp()
        self.childprop=float(input("enter the child prop value:"))
        self.totprop=self.pprop+self.childprop
        print("the parent prop is {}".format(self.pprop))
        print("the child prop is{}".format(self.childprop))
        print("the total prop is{}".format(self.totprop))
#main program
# co2=child()
# co2.disp()
# co2.disp1()