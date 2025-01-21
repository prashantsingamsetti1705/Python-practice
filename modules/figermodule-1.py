#here is the main program and conacting the differt file of which are module name are we importing
#figremodule are program name
from figmenu import menu
from circle import area_circle,perimeter_circle
from square import area_square,perimeter_square
from rectangle import area_rec,perimeter_rec
from trinagle import area_tri,perimeter_tri
from submenu import submenu
while True:
    menu()
    ch=input("enter your choice")
    if ch.isdigit():
        match(int(ch)):
            case 1:
                while True:
                    submenu("circle")
                    ch1=input("enter your choice")
                    if ch.isdigit():
                        match(ch1.upper()):
                            case "A":
                                area_circle()
                            case "P":
                                perimeter_circle()
                            case "M":
                                break
                            case _:
                                print("your enter choice is wrong")
            case 2:
                while True:
                    submenu("square")
                    ch1=input("enter your choice")
                    if ch.isdigit():
                        match(ch1.upper()):
                            case "A":
                                area_square()
                            case "P":
                                perimeter_square()
                            case "M":
                                break
                            case _:
                                print("your enter choice is wrong")
            case 3:
                while True:
                    submenu("rec")
                    ch1=input("enter your choice")
                    if ch.isdigit():
                        match(ch1.upper()):
                            case "A":
                                area_rec()
                            case "P":
                                perimeter_rec()
                            case "M":
                                break
                            case _:
                                print("your enter choice is wrong")
            case 4:
                while True:
                    submenu("tri")
                    ch1=input("enter your choice")
                    if ch.isdigit():
                        match(ch1.upper()):
                            case "A":
                                area_tri()
                            case "P":
                                perimeter_tri()
                            case "M":
                                break
                            case _:
                                print("your enter choice is wrong")
            case 5:
                print("this program is completed please exist")
                break
            case _:
                print("pelse enter the valid you had choosen wrong")
    else:
        print("Don't enter alnums,strs and symbols for int Choice-try again")