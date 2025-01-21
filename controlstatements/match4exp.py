import sys
print(" conversion of base ")
print("""1-
Dto b -- bin()
Dto o --oct()
Dto h ---hexa ()""")
print("""2- 
bto d -- bin()
bto o --oct()
bto h ---hexa ()""")
print("""3- 
oto d -- bin()
oto b--oct()
oto h ---hexa ()""")
print("""4-
hto d -- bin()
hto b --oct()
hto o ---hexa ()""")
print("5-Exit")
bc=int(input("enter your choice:"))
match bc:
    case 1:
        print("enter a decimal ")
        a=int(input("enter value of :"))
        print("{}is {}".format(a,bin(a)))
        print("{}is {}".format(a,oct(a)))
        print("{}is {}".format(a, hex(a)))
    case 2:
        print("enter a binary ")
        a=input("enter value of :")
        b=int(a,2)
        print("{}".format(a))
        print("{}is {}".format(a,oct(b)))
        print("{}is {}".format(a, hex(b)))
    case 3:
        print("enter a octal number ")
        o=input("enter value of :")
        b=int(o,8)
        print("{}".format(b))
        print("{}is {}".format(o,bin(b)))
        print("{}is {}".format(o, hex(b)))
    case 4:
        print("enter a hex number ")
        h=input("enter value of :")
        a=int(h,16)
        print("{}is {}".format( h,a))
        print("{}is {}".format(h, bin(a)))
        print("{}is {}".format(h, oct(a)))
    case 5:
        print("this program completed")
        sys.exit()
    case _:
        print("you had choocien wrong ")
print("this  match program has completed")













