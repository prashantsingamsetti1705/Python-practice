#write a python program which used delete the folder by using the os
#removedir()
import os
try:
    os.rmdir("pytho")#hre remove() of will remove only a one folder
    print("file deleted successfully please try again")
except FileExistsError:
    print("file is already exist please try again")
except FileNotFoundError:
    print("file does not exist please try again")

