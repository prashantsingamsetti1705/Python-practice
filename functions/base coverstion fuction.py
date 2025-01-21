#write a python program which will print the base conversion calculator
#menu of base converstion
def menu():
    print("Base converstion")
    print("*"*50)
    print(""" 1-DtoB---bin()
    DtoO-------oct()
    DtoH-------hex()
    """)
    print(""" 2-BtoD---automatic()
    BtoO-------oct()
    BtoH-------hex()
    """)
    print(""" 3-OtoD---automatic()
    OtoB-------bin()
    OtoH-------hex()
    """)
    print(""" 4-HtoD---automatic()
    HtoB-------bin()
    HtoO-------oct()
    """)
def decimal_value():#
    a=int(input("eneter a value of:"))
    print("{},{}".format(a,bin(a)))
    print("{},{}".format(a, oct(a)))
    print("{},{}".format(a,hex(a)))
def binary_value():
    b=input("enter a value of b:")
    a=int(b,2)
    print("{}".format(a))
    print("{},{}".format(a, oct(a)))
    print("{},{}".format(a,hex(a)))
def oct_value():
    o=input("enter a value of o:")
    a=int(o,8)
    print("{}".format(a,))
    print("{},{}".format(a, bin(a)))
    print("{},{}".format(a,hex(a)))
def hex_value():
    h=input("enter a value of o:")
    a=int(h,16)
    print("{}".format(a,))
    print("{},{}".format(a, bin(a)))
    print("{},{}".format(a,oct(a)))

#main program
while True:
    menu()
    ch=int(input("enter a your choice:"))
    match(ch):
        case 1:
            decimal_value()
        case 2:
            binary_value()
        case 3:
            oct_value()
        case 4:
            hex_value()
        case 5:
            print("thanks for using this program")
            break
        case _:
            print("enter your choiche wrong number")
    #logic-2
# def menu():
#     print("Base converstion")
#     print("*"*50)
#     print(""" 1-DtoB---bin()
#     DtoO-------oct()
#     DtoH-------hex()
#     """)
#     print(""" 2-BtoD---automatic()
#     BtoO-------oct()
#     BtoH-------hex()
#     """)
#     print(""" 3-OtoD---automatic()
#     OtoB-------bin()
#     OtoH-------hex()
#     """)
#     print(""" 4-HtoD---automatic()
#     HtoB-------bin()
#     HtoO-------oct()
#     """)
# def read_value:
#     a=int(input("enter a value a"))
#     return a
# def decimal_value():#
#     a=read_value()
#     print("{},{}".format(a,bin(a)))
#     print("{},{}".format(a, oct(a)))
#     print("{},{}".format(a,hex(a)))
# def binary_value():
#     b=input("enter a value of b:")
#     a=int(b,2)
#     print("{}".format(a))
#     print("{},{}".format(a, oct(a)))


#     print("{},{}".format(a,hex(a)))
# def oct_value():
#     o=input("enter a value of o:")
#     a=int(o,8)
#     print("{}".format(a,))
#     print("{},{}".format(a, bin(a)))
#     print("{},{}".format(a,hex(a)))
# def hex_value():
#     h=input("enter a value of o:")
#     a=int(h,16)
#     print("{}".format(a,))
#     print("{},{}".format(a, bin(a)))
#     print("{},{}".format(a,oct(a)))
#
# #main program
# while True:
#     menu()
#     ch=int(input("enter a your choice:"))
#     match(ch):
#         case 1:
#             decimal_value()
#         case 2:
#             binary_value()
#         case 3:
#             oct_value()
#         case 4:
#             hex_value()
#         case 5:
#             print("thanks for using this program")
#             break
#         case _:
#             print("enter your choiche wrong number")