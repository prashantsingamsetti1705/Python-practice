#write a python program of Aera of different figure
#enter to choice .
import sys
print("*"*50)
print("Are of Different figures")
print("*"*50)
print("R-Rectangle")
print("S-Square")
print("C-Circle")
print("T-Triangle")
print("E-Exit")
print("*"*50)
ar=input("enter your choice:")
match ar:
    case "r"|"R":
        print("enter  a any two values:")
        l,w=float(input("enter a value of lenght:")),float(input("enter a value of width:"))

        s=l*w
        print("{},{}={}".format(l,w,s))
    case "s|S" :
        s1=float(input("enter a value of s1:"))
        s2=float(input("enter a value of s2:" ))
        print("{},{}are of square{}".format(s1,s2,s1*s2))
    case "c"|"C":
        c1=float(input("enter a value of r1:"))
        c2=float(input("enter a value of r2:"))
        print("{},{}are of circle{}".format(c1, c2,3.14* c1 * c2))
    case "t"|"T":
        t1 = float(input("enter a value of t1:"))
        t2 = float(input("enter a value of t2:"))
        print("{},{}are of triangle{}".format(t1, t2, 0.5* t1 * t2))
    case "e"|"E":
        print("this is completed")
        sys.exit()
    case _:
        print("you had chocicen worng try again")
print("matched is completed")