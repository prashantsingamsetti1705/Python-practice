#write a python program which is used to delet the filename
import os
try:
    os.remove("C:\\Users\\prash\\PycharmProjects\\OSmodel\\sai\\raju\\prash\\anil\\emp.py")
    print("file deteled successfully")
except FileNotFoundError:
    print("file does not exsit please try again")