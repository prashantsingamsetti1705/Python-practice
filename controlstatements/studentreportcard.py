#write a python program which will print student number student name student sub merks totalmarks and percentage and grade
#validation of student number
while True:
    sn=input("enter a student number:")
    if sn.isdigit() and int(sn) in range(100,201):
        break
    else:
        print("{} is invalid student number".format(sn))
#validation of the student name
while True:
    sn1=input("enter a student name:")
    words=sn1.split()
    nv=True
    for word in words:
        if not word.isalpha():
            nv=False
            break
    if nv:
        break
    else:
        print("\t\t is invalid name:".format(sn1))
#validation of student marks
while True:
    c=input("enter a student mark of c:")
    if c.isdigit() and int(c) in range(0,101):
        break
    else:
        print("{} is invalid student number".format(c))
while True:
    cp=input("enter a student mark of cp:")
    if cp.isdigit() and int(cp) in range(0,101):
        break
    else:
        print("{} is invalid student number".format(cp))
while True:
    py=input("enter a student mark of py:")
    if c.isdigit() and int(c) in range(0,101):
        break
    else:
        print("{} is invalid student number".format(py))
#validation of total marks
tm=int(c)+int(cp)+int(py)
pc=(tm/300)*100
#validation of grade
if int(c)<40 or int(cp)<40 or int(py)<40:
     grade="fail"
else:
     if pc in range(75,101):
         grade="distinction"
     elif pc in range(76,60):
         grade="first"
     elif(50<=pc<=59):
         grade="second"
     elif(pc in range(40,49)):
         grade="third"
print("*"*70)
print("*"*70)
print("\t\tSTUDENT MARKS REPORT")
print("*"*70)
print("\t\tStudent Number:{}".format(sn))
print("\t\tStudent Name:{}".format(sn1))
print("\t\tStudent Marks in C:{}".format(c))
print("\t\tStudent Marks in C++:{}".format(cp))
print("\t\tStudent Marks in PYTHON:{}".format(py))
print("\t\tStudent Total Marks:{}".format(tm))
print("\t\tStudent Percentage of Marks:{}".format(pc))
print("\t\tstudent grade:{}".format(grade))