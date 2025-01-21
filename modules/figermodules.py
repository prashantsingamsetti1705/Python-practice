#here is the main program and conacting the differt file of which are module name are we importing
#figremodule are program name
from figmenu import menu
from circle import area_circle,perimeter_circle
from square import area_square,perimeter_square
from rectangle import area_rec,perimeter_rec
from trinagle import area_tri,perimeter_tri
while True:
    menu()
    ch=input("enter your choice")
    if ch.isdigit():
        match(int(ch)):
            case 1:
                area_circle()
                perimeter_circle()
            case 2:
                area_square()
                perimeter_square()
            case 3:
                area_rec()
                perimeter_rec()
            case 4:
                area_tri()
                perimeter_tri()
            case 5:
                print("this program is completed please exist")
                break
            case _:
                print("pelse enter the valid you had choosen wrong")
    else:
        print("Don't enter alnums,strs and symbols for int Choice-try again")