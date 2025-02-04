#write a python program which is ued to alter the table modify,add by connetion of oracle db
import oracledb as orc
def dbalter():
    try:
        #step2
        con_obj=orc.connect("system/1705@localhost/XE")
        #step3
        cu=con_obj.cursor()
        #step4
        q=input("enter the query which u want to modify the query:")
        #step5
        cu.execute(q)
        print("query is modify successfully---verify")
    except orc.DatabaseError:
        print("there is problem in oracle db pleae check it")
dbalter()