#write a python program to choice a any one temperature conversion calculator
#program by using match case
import sys
print("*"*50)
print("temperature Conversion Calculator")
print("*"*50)
print("1-F to C")
print("2-F to K")
print("3-C to F")
print("4-C to k")
print("5-K to F")
print("6-K to C")
print("7-Exit")
print("*"*50)
tc=int(input("Enter your choice:"))
match tc:
    case 1:
        print("enter  two values of f&c:")
        f,c=float(input("enter a temp of f:")),float(input("enter a temp of c:"))
        print("{} is {} of f to c {} ".format(f,c,(f-32) * (5/9)))
    case 2:
        print("enter  two values of f&k:")
        f, k = float(input("enter a temp of f:")), float(input("enter a temp of k:"))
        print("{} is {} of f to k {} ".format(f, k, (f - 32) *( 5 / 9 )+ 273.15))
    case 3:
        print("enter  two values of c&f:")
        c, f = float(input("enter a temp of c:")), float(input("enter a temp of f:"))
        print("{} is {} of c to f {} ".format(c, f, c*( 5 / 9)+32))

    case 4:
        print("enter  two values of c&k:")
        c, k = float(input("enter a temp of c:")), float(input("enter a temp of k:"))
        print("{} is {} of c to k {} ".format(c, k, c + 273.15))
    case 5:
        print("enter  two values of k&c:")
        k, c = float(input("enter a temp of K:")), float(input("enter a temp of c:"))
        print("{} is {} of k to c {} ".format(k, c, k  - 273.15))
    case 6:
        print("enter  two values of k&f:")
        k, f = float(input("enter a temp of K:")), float(input("enter a temp of f:"))
        print("{} is {} of k to f {} ".format(k, f, (k - 273.15 * 9/5) + 32))
    case 7:
        print("this program is completed")
        sys.exit()
    case _:
        print("you are chocine worng plese try again")
print("this matched is completed")
