# write a python program which is ued to delete the data from the record dynamically
import oracledb as orc
#step1
def delrec():
    while True:
        try:
            con_obj=orc.connect("system/1705@localhost/XE")
            cu=con_obj.cursor()
            eno=int(input("enter the query which you wnt to delete the record enter the eno:"))
            cu.execute("delete from empolyess where eno=%d" %eno)
            con_obj.commit()
            if cu.rowcount>0:
                print("the record is deleted sucessfully please --->verfiy {}".format(cu.rowcount))
            else:
                print("the record is empty no of {}".format(cu.rowcount))
            ch=input("are will to delete the other records presnt init (yes/no):")
            if ch.lower()=="no":
                print("thanks for using this program")
                break
        except ValueError:
            print("dont enter the alnums for ")
        except orc.DatabaseError as db:
            print("ther is problem in your oracle db --{}".format(db))
delrec()


