#write a python program which will implement the following
import sys
print("*"*5)
print("Arthamatic operartion")
print("*"*50)
print("1-Addition")
print("2-subtarcation")
print("3-Multiplication")
print("4-Division/follor Division")
print("5-moduloDivision")
print("6-base exponential operator")
print("7-exit")
print("*"*50)
n=int(input("choice an operator"))
match n:
    case 1|11:
        print("enter a two values ")
        a,b=float(input("enetr value of a :")),float(input("enter value of b:"))
        print("{} {} addition {}".format(a,b,a+b))
    case 2|22:
        print("enter a two values :")
        a,b=float(input("enetr value of a")), float(input("enter value of b"))
        print("{} {} subraction {}".format(a, b, a-b))
    case 3|33:
        print("enter a two values :")
        a, b = float(input("enetr value of a")), float(input("enter value of b"))
        print("{} {} mul {}".format(a, b, a*b))
    case 4|44:
        print("enter a two values :")
        a, b = float(input("enetr value of a")), float(input("enter value of b"))
        print("{} {} div {}".format(a, b, a/b))
    case 5|55:
        print("enter a two values :")
        a, b = float(input("enetr value of a")), float(input("enter value of b"))
        print("{} {} modulo {}".format(a, b, a//b))
    case 6|66:
        print("enter a two values :")
        a, b = float(input("enetr value of a")), float(input("enter value of b"))
        print("{} {} base expo {}".format(a, b, a**b))
    case 7|77:
        print("this is completed")
        sys.exit()
    case _:
        print(" you are chooicen wrong----try again")
print("matched  case completed")


