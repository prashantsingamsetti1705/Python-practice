#write a python program which is used to delete the data from the record from key bord and dynamically
#step1
import oracledb as orc
def recdel():
    try:
        #step2
        con_obj=orc.connect("system/1705@localhost/XE")
        #step3
        cu=con_obj.cursor()
        #step
        dq="delete empolyess where eno=100"
        cu.execute(dq)
        con_obj.commit()
        print("record is delted successfully--->verify")
    except orc.DatabaseError as db:
        print("their is problem in your please check it --->db{}".format(db))
recdel()

