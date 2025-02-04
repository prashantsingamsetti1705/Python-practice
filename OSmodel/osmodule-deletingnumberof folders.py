#write a python program which used to delete the number of folders
import os
try:
    os.removedirs("sai\\raju\\prash\\anil")
    print("folders deleted successfully please ---------> verfiy")
except FileNotFoundError:
    print("file does not exist please try again")

