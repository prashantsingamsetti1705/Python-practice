#wriet a python program wchish is used to genarate a a line of alphabets into lower case and annd upsercase

def lower(ol):
    def op1():
        line,upper=ol()
        lower=line.lower()
        return line,upper,lower
    return op1
def upper(up):
    def op():
        line=up()
        upper=line.upper()
        return line,upper
    return op
@lower
@upper
def line():
    line=input("enter the line whcih you want to generate the line of loer case and upcas")
    return line
line,upper,lower=line()
print("given line:",line)
print("upper=",upper)
print("lower=",lower)