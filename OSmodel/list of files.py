#write a python which uesd to print the list of number of files
#listdir
import os
try:
    lst=os.listdir("C:\\Users\\prash\\PycharmProjects\\OSmodel")
    print("no of file in a list")
    no=0
    for val in lst:
        print(val)
        no=no+1

    print("no of files=",no)
except FileNotFoundError:
    print("file does not exist")

