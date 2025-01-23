#write a python program for demonstrating the program
#file readlines()
try:
    with open("prash.text","r") as fp:
        lines=fp.readlines()
        print("*50"*50)
        print(lines)
        print(type(lines))#<class 'list'>
        print("*"*50)
except FileNotFoundError:
    print("file does not exist")
