#writea python program which read the file
try:
    fp=open("stud1.txt","r")
except FileNotFoundError:
    print("file does not exist")
else:
    print("*" * 50)
    print("iam from the else block")
    print("file open succesfully")
    print("type of fp",type(fp))
    print("is file is closed=",fp.closed)
finally:
    try:
        print("iam from the finally block")
        fp.close()#Manually Closing
        print("file close safely",fp.close())
        print("*"*50)
    except NameError:
        print("you the defind the var name")
