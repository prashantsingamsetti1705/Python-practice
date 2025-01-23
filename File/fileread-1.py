#python program which read the file
try:
    with open("prash.text","r") as fp:
        lines=fp.read()
        print("*"*50)
        print(lines)
        print(type(lines))#<class 'str'>
        print("*"*50)
except FileNotFoundError:
    print("file does not exist")