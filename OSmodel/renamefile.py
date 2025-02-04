#write a python program which used to change the filename
#rename()
import os
try:
    os.rename("empy.py","emp2.py")
    print("file name change successfully ------->verify")
except FileNotFoundError:
    print("file does not exist")
