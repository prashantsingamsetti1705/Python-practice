#writre a python python program which create a number of folder by using the os
import os
try:
    os.makedirs("sai\\raju\\prash\\anil")
    print("file created successfully---->verify ")
except FileExistsError:
    print("file is already exist please try again")
