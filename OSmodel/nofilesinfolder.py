#write a python which uesd to print the list of number of files
#listdir
import os
try:
    lst=os.listdir("C:\\Users\\prash\\PycharmProjects\\OSmodel")
    print("no of file in a list")
    for val in lst:
        print(val)
except FileNotFoundError:
    print("file does not exist")