#write a python program for read and write  the adata on e record to another record
#write(str())

while True:
    print("*"*50)
    eno=int(input("enter the empolyee number:"))
    en=input("enter the empolyee name:")
    sal=float(input("enter the your salary"))
    print("*" * 50)
    with open("record2.txt","a") as fp:
        fp.write(str(eno)+"\t")
        fp.write(en+"\n")
        fp.write(str(sal)+"\n")
        print("the value are enter the new record")
        print("*" * 50)
        ch=input("enter yor choes is (yes/no):")
        if ch.lower()=="no":
            print("thans for using this program")
            break

