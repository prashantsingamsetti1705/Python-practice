#wite a python program which is used to insert the data into table
import oracledb as orc
def dbinsert():
    try:
        #step2
        con_obj=orc.connect("system/1705@localhost/XE")
        #step3
        cu=con_obj.cursor()
        #step4
        q=input("eneter the query to insert the data int table")
        #step5
        cu.execute(q)
        print("value are insert into tbale successfully please verify")
        con_obj.commit()
    except orc.DatabaseError as db:
        print("there is problem in oracle--db plese check it",db)
#main program
dbinsert()