#write a python program which create a new file using w mode and attributes
with open("stud2.txt","a+") as fp:
    print("file created as w mode")
    print("*"*50)
    print("file closed=", fp.closed)
    print("file attributes")
    print("filename=",fp.name)
    print("filemode=",fp.mode)
    print("file readable=",fp.readable())
    print("file writable=",fp.writable())
print("iam out the with open")
print("file closed=",fp.closed)