#write a python program of the sample example on the hybird in heritance
class grandparent:
    def getparent(self):
        self.gppop=float(input("enter the prop of the grandparent"))
class father(grandparent):
    def grtfather(self):
        self.fatherprop=float(input("enter the prop of the father"))
class mother(father):
    def getmother(self):
        self.motherprop=float(input("enter the prop of the mother"))
class child(mother):
    def getchild(self):
        self.childprop=float(input("enter the prop of the child"))
    def dispprop(self):
        self.totalprop=self.gppop+self.fatherprop+self.motherprop+self.childprop
        print("the prop of the grand parent{}".format(self.gppop))
        print("the prop of the father {}".format(self.fatherprop))
        print("the prop of the mother {}".format(self.motherprop))
        print("the prop of the child {}".format(self.childprop))
        print("the total prop--->{}".format(self.totalprop))
#main program
co3=child()
co3.getparent()
co3.grtfather()
co3.getmother()
co3.getchild()
co3.dispprop()