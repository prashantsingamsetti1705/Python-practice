#Prpogram for Cal addiution of Two Numbers by using Anonymous Function
#AnonymousFunEx1.py
addop=lambda a,b:a+b

#Main Program
print("Type of addop=",type(addop)) # <class 'function'>
print("--------------------------------------")
print("Enter Two Values")
res=addop(float(input()),float(input()))
print("Sum By using Anomynous Function=",res)

##Program for Performfing all arithmetic Operations by using Anonymous Functions
#AnonymousFunEx1.py
import sys
sumop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
fdivop=lambda a,b:a//b
modop=lambda a,b:a%b
expop=lambda a,b:a**b

print("*"*50)
print("\tArithmetic Operations")
print("*"*50)
print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Div")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")
print("*"*50)
ch=int(input("Enter UR Choice:"))
match(ch):
    case 1 :
        print("Enter Two Values for Addition:")
        a,b=float(input()),float(input())
        print("\t\tsum({},{})={}".format(a,b,sumop(a,b)))
    case 2:

        print("Enter Two Values for Substraction:")
        a, b = float(input()), float(input())
        print("\t\tsub({},{})={}".format(a, b, subop(a,b)))
    case 3:
        print("Enter Two Values for Multiplication:")
        a, b = float(input()), float(input())
        print("\t\tmul({},{})={}".format(a, b, mulop(a , b)))
    case 4:
        print("Enter Two Values for Division:")
        a, b = float(input()), float(input())
        print("\t\tNormal Div({},{})={}".format(a, b, divop(a,b)))
        print("\t\tFloor Div({},{})={}".format(a, b, fdivop(a,b)))
    case 5:
        print("Enter Two Values for Modulo Div:")
        a, b = float(input()), float(input())
        print("\t\tmod({},{})={}".format(a, b, modop(a,b)))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("\t\tpow({},{})={}".format(a, b, expop(a,b)))
    case 7:
        print("Thx for Using this Program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong--try again")





