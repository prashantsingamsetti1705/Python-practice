#write a python  program on the single inheritance
class Parent:
    def disp(self):
        self.prop=10
class Child(Parent):
    def disp1(self):
        self.childprop=0.5
        self.totprop=self.prop+self.childprop
        print("the property of the parent{}".format(self.prop))
        print("the prperty of the child is{}".format(self.childprop))
        print("the total property of is {}".format(self.totprop))
#mainprogram
co2=Child()
co2.disp()
co2.disp1()