#write apython program which will choosemenu option of arthematic operation
def menu_arthematic():#define function
    print("*"*50)
    print("ARTHEMATIC OPERATION")
    print("*"*50)
    print("1--->addition'+'")
    print("2--->subraction'-'")
    print("3--->mul'*'")
    print("4--->division'/','//'")
    print("5--->modulo division'%'")
    print("6--->eponentional'**'")
    print("7--->exit")
    print("-"*50)
def read_value():
    a,b=int(input("enter value of a:")),int(input("enter value ofb:"))
    return a,b
def addop():
    a,b=read_value()
    print("addtion of a,b-is-->({},{})={}".format(a,b,a+b))
def subop():
    a,b=read_value()
    print("sub of a,b-is-->({},{})={}".format(a,b,a-b))
def mulop():
    a,b=read_value()
    print("mul of a,b-is-->({},{})={}".format(a,b,a*b))
def divop():
    a,b=read_value()
    print("div of a,b-is-->({},{})={}".format(a,b,a/b))
    print("div of a,b-is--->({},{})={}".format(a,b,a//b))
def modop():
    a,b=read_value()
    print("mod of a,b-is-->({},{})={}".format(a,b,a%b))
def exop():
    a,b=int(input("enter a vlue of base a:")),int(input("enter a value of power b:"))
    print("sub of a,bis-->({},{})={}".format(a,b,a-b))
#main program
while True:
    menu_arthematic()#function call
    ch=input("enter your choice:")
    match(int(ch)):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            exop()
        case 7:
            print("tahnkyou for using this program")
            break
        case _:
            print("you had choochen wrong menu")


