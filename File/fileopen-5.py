#write a python program which is ued to read and write  with open as :
#with open()as:
try:
    with open("stud2.txt","r+") as fp:
        print("file createde as read and write in r+mode")
        print("file is closed=", fp.closed)
        print("type of file=",type(fp))
        print("file properties")
        print("file name=",fp.name)
        print("file mode=",fp.mode)
        print("file raedable=",fp.readable())
        print("file witeable=",fp.writable())
    print("iam from the out indentation")
    print("file is cloed=",fp.closed)
except FileNotFoundError:
    print("file does not exist")