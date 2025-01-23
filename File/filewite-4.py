#Program for Reading the Data from KBD and Write It to the File
#FileWriteEx4.py
with open("prash.text","a") as fp:
    print("Enter Information and Press( @ to stop ):")
    while(True):
        kbdata=input()
        if(kbdata!="@"):
            fp.write(kbdata+"\n")
        else:
            print("Data written to the File--verify")
            break
