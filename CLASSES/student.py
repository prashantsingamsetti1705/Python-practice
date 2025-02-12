#write a python program of the the opps through the file while usimg the pickel
class student:
    def getstudvalues(self,sno,sname,marks):
        self.sno=sno
        self.sname=sname
        self.marks=marks
    def studvalues(self):
        print("{}\t{}\t{}".format(self.sno,self.sname,self.marks))
