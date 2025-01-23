#write a python program for demostrating the python program
#file readlines()
try:
    rp=input("entter the file name:")
    with open(rp,"r") as fp:
        lines=fp.readlines()
        for data in lines:
            print(data,end="")
        print()
except FileNotFoundError:
    print("file does not exist error")