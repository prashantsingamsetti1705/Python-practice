# write a python program to display course name and is devloped names
#using simple if
cn=input("enter a course name:")
if cn.lower()=="cp":
    print("C-program  is developed by dennis ritchie ")
if cn.lower()=="c":
    print("C++-program  is developed by bjarne stroustrup ")
if cn.lower()=="p":
    print("Python program is  developed by gudio van rossum")
if cn.lower()=="ja":
    print("Java program is  developed by james gosling ")
if cn.lower() not in ["cp","c","p","java"]:
    print("not in given course")













